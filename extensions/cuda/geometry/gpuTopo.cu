//-*- coding: utf-8 -*-
//
// Author: Bryan V. Riel, Joshua Cohen
// Copyright: 2017-2018

// isce::cuda::core
#include "isce/cuda/core/gpuEllipsoid.h"
#include "isce/cuda/core/gpuOrbit.h"
#include "isce/cuda/core/gpuPoly2d.h"
#include "isce/cuda/core/gpuPixel.h"
#include "isce/cuda/core/gpuBasis.h"
#include "isce/cuda/core/gpuStateVector.h"
// isce::cuda::product
#include "isce/cuda/product/gpuImageMode.h"
// isce::cuda::geometry
#include "gpuDEMInterpolator.h"
#include "gpuGeometry.h"
#include "gpuTopoLayers.h"
#include "gpuTopo.h"
using isce::cuda::core::gpuLinAlg;

#define THRD_PER_BLOCK 96 // Number of threads per block (should always %32==0)

__device__
bool initAzimuthLine(size_t line,
                     const isce::cuda::product::gpuImageMode & mode,
                     const isce::cuda::core::gpuOrbit & orbit,
                     isce::cuda::core::gpuStateVector & state,
                     isce::cuda::core::gpuBasis & TCNbasis) {

    // Get satellite azimuth time
    const double tline = mode.startAzUTCTime() + 
                         mode.numberAzimuthLooks() * line / mode.prf();

    // Interpolate orbit (keeping track of validity without interrupting workflow)
    bool valid = (orbit.interpolateWGS84Orbit(tline, state.position, state.velocity) == 0);

    // Cache pointers to the TCN basis components
    double * that = TCNbasis.x0;
    double * chat = TCNbasis.x1;
    double * nhat = TCNbasis.x2;

    // Compute geocentric TCN basis
    double temp[3];
    gpuLinAlg::unitVec(state.position, nhat);
    gpuLinAlg::scale(nhat, -1.0);
    gpuLinAlg::cross(nhat, state.velocity, temp);
    gpuLinAlg::unitVec(temp, chat);
    gpuLinAlg::cross(chat, nhat, temp);
    gpuLinAlg::unitVec(temp, that);

    return valid;
}

__device__
void setOutputTopoLayers(const double * targetLLH,
                         isce::cuda::geometry::gpuTopoLayers & layers,
                         size_t index, int lookSide,
                         const isce::cuda::core::gpuPixel & pixel,
                         const isce::cuda::core::gpuStateVector & state,
                         const isce::cuda::core::gpuBasis & TCNbasis,
                         isce::cuda::core::ProjectionBase ** projOutput,
                         const isce::cuda::core::gpuEllipsoid & ellipsoid,
                         const isce::cuda::geometry::gpuDEMInterpolator & demInterp) {

    double targetXYZ[3], satToGround[3], enu[3];
    double enumat[9], xyz2enu[9];
    const double degrees = 180.0 / M_PI;

    // Convert lat/lon values to output coordinate system
    double xyzOut[3];
    (*projOutput)->forward(targetLLH, xyzOut);
    const double x = xyzOut[0];
    const double y = xyzOut[1];

    // Set outputs
    layers.x(index, x);
    layers.y(index, y);
    layers.z(index, targetLLH[2]);

    // Convert llh->xyz for ground point
    ellipsoid.lonLatToXyz(targetLLH, targetXYZ);

    // Compute vector from satellite to ground point
    gpuLinAlg::linComb(1.0, targetXYZ, -1.0, state.position, satToGround);

    // Computation in ENU coordinates around target
    gpuLinAlg::enuBasis(targetLLH[1], targetLLH[0], enumat);
    gpuLinAlg::tranMat(enumat, xyz2enu);
    gpuLinAlg::matVec(xyz2enu, satToGround, enu);
    const double cosalpha = std::abs(enu[2]) / gpuLinAlg::norm(enu);

    // LOS vectors
    layers.inc(index, std::acos(cosalpha) * degrees);
    layers.hdg(index, (std::atan2(-enu[1], -enu[0]) - (0.5*M_PI)) * degrees);

    // East-west slope using central difference
    double aa = demInterp.interpolateXY(x - demInterp.deltaX(), y);
    double bb = demInterp.interpolateXY(x + demInterp.deltaX(), y);
    double gamma = targetLLH[1];
    double alpha = ((bb - aa) * degrees) / (2.0 * ellipsoid.rEast(gamma) * demInterp.deltaX());

    // North-south slope using central difference
    aa = demInterp.interpolateXY(x, y - demInterp.deltaY());
    bb = demInterp.interpolateXY(x, y + demInterp.deltaY());
    double beta = ((bb - aa) * degrees) / (2.0 * ellipsoid.rNorth(gamma) * demInterp.deltaY());

    // Compute local incidence angle
    const double enunorm = gpuLinAlg::norm(enu);
    for (int idx = 0; idx < 3; ++idx) {
        enu[idx] = enu[idx] / enunorm;
    }
    double costheta = ((enu[0] * alpha) + (enu[1] * beta) - enu[2])
                     / std::sqrt(1.0 + (alpha * alpha) + (beta * beta));
    layers.localInc(index, std::acos(costheta)*degrees);

    // Compute amplitude simulation
    double sintheta = std::sqrt(1.0 - (costheta * costheta));
    bb = sintheta + 0.1 * costheta;
    layers.sim(index, std::log10(std::abs(0.01 * costheta / (bb * bb * bb))));

    // Calculate psi angle between image plane and local slope
    double n_img[3], n_imghat[3], n_img_enu[3], n_trg_enu[3];
    gpuLinAlg::cross(satToGround, state.velocity, n_img);
    gpuLinAlg::unitVec(n_img, n_imghat);
    gpuLinAlg::scale(n_imghat, -1*lookSide);
    gpuLinAlg::matVec(xyz2enu, n_imghat, n_img_enu);
    n_trg_enu[0] = -alpha;
    n_trg_enu[1] = -beta;
    n_trg_enu[2] = 1.0;

    const double cospsi = gpuLinAlg::dot(n_trg_enu, n_img_enu) /
                         (gpuLinAlg::norm(n_trg_enu) * gpuLinAlg::norm(n_img_enu));
    layers.localPsi(index, std::acos(cospsi) * degrees);
}

__global__
void runTopoBlock(isce::cuda::core::gpuEllipsoid ellipsoid,
                  isce::cuda::core::gpuOrbit orbit,
                  isce::cuda::core::gpuPoly2d doppler,
                  isce::cuda::product::gpuImageMode mode,
                  isce::cuda::geometry::gpuDEMInterpolator demInterp,
                  isce::cuda::core::ProjectionBase ** projInput,
                  isce::cuda::core::ProjectionBase ** projOutput,
                  isce::cuda::geometry::gpuTopoLayers layers,
                  size_t lineStart, int lookSide, double threshold,
                  int numiter, int extraiter) {

    // Get the flattened index
    size_t index_flat = (blockDim.x * blockIdx.x) + threadIdx.x;
    const size_t NPIXELS = layers.length() * layers.width();

    // Give gpuDEMInterpolator object a pointer to input projection on the device
    demInterp.proj(projInput);

    // Only process if a valid pixel (while trying to avoid thread divergence)
    if (index_flat < NPIXELS) {

        // Unravel the flattened pixel index
        const size_t line = index_flat / layers.width();
        const size_t rbin = index_flat - line * layers.width();
        
        // Interpolate orbit (keeping track of validity without interrupting workflow)
        isce::cuda::core::gpuStateVector state;
        isce::cuda::core::gpuBasis TCNbasis;
        bool valid = (initAzimuthLine(line + lineStart, mode, orbit, state, TCNbasis) != 0);

        // Compute magnitude of satellite velocity
        const double satVmag = gpuLinAlg::norm(state.velocity);

        // Get current slant range
        const double rng = mode.startingRange() + rbin * mode.rangePixelSpacing();
        
        // Get current Doppler value and factor
        const double dopval = doppler.eval(0, rbin);
        const double dopfact = 0.5 * mode.wavelength() * (dopval / satVmag) * rng;

        // Store slant range bin data in gpuPixel
        isce::cuda::core::gpuPixel pixel(rng, dopfact, rbin);
        
        // Initialize LLH to middle of input DEM and average height
        double llh[3];
        demInterp.midLonLat(llh);
        
        // Perform rdr->geo iterations
        int geostat = isce::cuda::geometry::rdr2geo(
            pixel, TCNbasis, state, ellipsoid, demInterp, llh, lookSide,
            threshold, numiter, extraiter
        );

        // Save data in output arrays
        setOutputTopoLayers(llh, layers, index_flat, lookSide, pixel, state, TCNbasis,
                            projOutput, ellipsoid, demInterp);
    }
}

// Create ProjectionBase pointer on the device (meant to be run by a single thread)
__global__
void
createProjection(isce::cuda::core::ProjectionBase ** projInput, int inputEpsgCode,
                 isce::cuda::core::ProjectionBase ** projOutput, int outputEpsgCode) {
    if (threadIdx.x == 0 && blockIdx.x == 0) {
        (*projInput) = isce::cuda::core::createProj(inputEpsgCode);
        (*projOutput) = isce::cuda::core::createProj(outputEpsgCode);
    }
}

// Delete ProjectionBase pointer on the device (meant to be run by a single thread)
__global__
void
deleteProjection(isce::cuda::core::ProjectionBase ** projInput,
                 isce::cuda::core::ProjectionBase ** projOutput) {
    delete *projInput;
    delete *projOutput;
}

// C++ Host code for launching kernel to run topo on current block
void isce::cuda::geometry::
runGPUTopo(const isce::core::Ellipsoid & ellipsoid,
           const isce::core::Orbit & orbit,
           const isce::core::Poly2d & doppler,
           const isce::product::ImageMode & mode,
           isce::geometry::DEMInterpolator & demInterp,
           isce::geometry::TopoLayers & layers,
           size_t lineStart, int lookSide, int epsgOut,
           double threshold, int numiter, int extraiter) {

    // Set the device
    //cudaSetDevice(0);

    // Create gpu ISCE objects
    isce::cuda::core::gpuEllipsoid gpu_ellipsoid(ellipsoid);
    isce::cuda::core::gpuOrbit gpu_orbit(orbit);
    isce::cuda::core::gpuPoly2d gpu_doppler(doppler);
    isce::cuda::product::gpuImageMode gpu_mode(mode); 
    isce::cuda::geometry::gpuDEMInterpolator gpu_demInterp(demInterp); 
    isce::cuda::geometry::gpuTopoLayers gpu_layers(layers);
    
    // Allocate projection pointers on device
    isce::cuda::core::ProjectionBase **projInput_d, **projOutput_d;
    checkCudaErrors(cudaMalloc(&projInput_d, sizeof(isce::cuda::core::ProjectionBase **)));
    checkCudaErrors(cudaMalloc(&projOutput_d, sizeof(isce::cuda::core::ProjectionBase **)));
    createProjection<<<1, 1>>>(projInput_d, demInterp.epsgCode(), projOutput_d, epsgOut);

    // Determine grid layout
    dim3 block(THRD_PER_BLOCK);
    const size_t npixel = layers.length() * layers.width();
    const int nBlocks = (int) std::ceil((1.0 * npixel) / THRD_PER_BLOCK);
    dim3 grid(nBlocks);

    // Launch kernel
    runTopoBlock<<<grid, block>>>(gpu_ellipsoid, gpu_orbit, gpu_doppler, gpu_mode,
                                  gpu_demInterp, projInput_d, projOutput_d, gpu_layers,
                                  lineStart, lookSide, threshold, numiter, extraiter);

    // Check for any kernel errors
    checkCudaErrors(cudaPeekAtLastError());

    // Copy results back to host
    gpu_layers.copyToHost(layers);

    // Delete projection pointer on device
    deleteProjection<<<1, 1>>>(projInput_d, projOutput_d);

    // Free projection pointer
    checkCudaErrors(cudaFree(projInput_d));
    checkCudaErrors(cudaFree(projOutput_d));
}

// end of file
