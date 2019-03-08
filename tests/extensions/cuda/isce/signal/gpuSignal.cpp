#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>
#include <valarray>
#include <complex>
#include <cufft.h>
#include <cufftXt.h>
#include <gtest/gtest.h>

#include "isce/signal/Signal.h"
#include "isce/io/Raster.h"

#include "isce/cuda/signal/gpuSignal.h"
#include "isce/cuda/core/gpuComplex.h"

// debug
#include <fstream>

using isce::cuda::signal::gpuSignal;
using isce::cuda::core::gpuComplex;

TEST(gpuSignal, ForwardBackwardRangeFloatDevMem)
{
    // take a block of data, perform range FFT and then iverse FFT and compare with original data   
    isce::io::Raster inputSlc("../../../../lib/isce/data/warped_envisat.slc.vrt");

    int width = inputSlc.width();
    int blockLength = inputSlc.length();
    gpuComplex<float> *d_data;

    // reserve memory for a block of data
    std::valarray<std::complex<float>> data(width*blockLength);

    // reserve memory for a block of data computed from inverse FFT
    std::valarray<std::complex<float>> inverted_data(width*blockLength);
    
    // read a block of data
    inputSlc.getBlock(data, 0, 0, width, blockLength);

    // copy data to device
    cudaError_t oops;
    size_t data_sz = width * blockLength * sizeof(gpuComplex<float>);
    oops = cudaMalloc(reinterpret_cast<void **>(&d_data), data_sz);
    oops = cudaMemcpy(d_data, &data[0], data_sz, cudaMemcpyHostToDevice);

    // a signal object
    gpuSignal<float> sig(CUFFT_C2C);

    // create the plan
    sig.rangeFFT(width, blockLength);

    sig.forwardDevMem(reinterpret_cast<float *>(d_data));
    sig.inverseDevMem(reinterpret_cast<float *>(d_data));

    cudaMemcpy(&inverted_data[0], d_data, data_sz, cudaMemcpyDeviceToHost);
   
    //normalize the result of inverse fft 
    inverted_data /=width;

    int blockSize = width*blockLength;
    std::complex<float> err(0.0, 0.0);
    bool Test = true;
    double max_err = 0.0;
    for ( size_t i = 0; i < blockSize; ++i ) {
        err = inverted_data[i] - data[i];
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    ASSERT_LT(max_err, 1.0e-4);
}
/*
TEST(gpuSignal, UpsampleDevMem)
{
    // take a block of data, perform range FFT and then iverse FFT and compare with original data   
    isce::io::Raster inputSlc("../../../../lib/isce/data/warped_envisat.slc.vrt");

    int width = inputSlc.width();
    int blockLength = inputSlc.length();
    gpuComplex<float> *d_data;

    // reserve memory for a block of data
    std::valarray<std::complex<float>> data(width*blockLength);

}
*/

TEST(gpuSignal, ForwardBackwardRangeFloatNoCp)
{
    // take a block of data, perform range FFT and then iverse FFT and compare with original data   
    isce::io::Raster inputSlc("../../../../lib/isce/data/warped_envisat.slc.vrt");

    int width = inputSlc.width();
    int length = inputSlc.length();

    // 
    int blockLength = length;

    // reserve memory for a block of data
    std::valarray<std::complex<float>> data(width*blockLength);

    // reserve memory for the spectrum of the block of data
    std::valarray<std::complex<float>> range_spectrum(width*blockLength);

    // reserve memory for a block of data computed from inverse FFT
    std::valarray<std::complex<float>> inverted_data(width*blockLength);
    
    // read a block of data
    inputSlc.getBlock(data, 0, 0, width, blockLength);

    // a signal object
    gpuSignal<float> sig(CUFFT_C2C);

    // create the plan
    sig.rangeFFT(width, blockLength);

    // copy data to device
    sig.dataToDevice(data);
   
    // forward fft transform
    sig.forwardC2C();

    // inverse fft transform
    sig.inverseC2C();

    // copy data to device
    sig.dataToHost(inverted_data);
   
    //normalize the result of inverse fft 
    inverted_data /=width;

    int blockSize = width*blockLength;
    std::complex<float> err(0.0, 0.0);
    bool Test = true;
    double max_err = 0.0;
    for ( size_t i = 0; i < blockSize; ++i ) {
        err = inverted_data[i] - data[i];
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    ASSERT_LT(max_err, 1.0e-4);
}

TEST(gpuSignal, upsampleDoubleNoCp)
{
    int width = 100;
    int length = 1;
    int blockLength = length;

    // fft length for FFT computations
    size_t nfft;

    //sig.nextPowerOfTwo(width, nfft);
    nfft = width;
    // upsampling factor
    int oversample = 2;

    // reserve memory for a block of data with the size of nfft
    std::valarray<std::complex<double>> slc(nfft);
    std::valarray<std::complex<double>> slcU(nfft*oversample);

    for (size_t i=0; i<width; ++i){
        double phase = std::sin(10*M_PI*i/width);
        slc[i] = std::complex<double> (std::cos(phase), std::sin(phase));
    }

    // instantiate a signal object
    gpuSignal<double> sig_lo_res(CUFFT_Z2Z);
    gpuSignal<double> sig_hi_res(CUFFT_Z2Z);

    // create plans
    sig_lo_res.rangeFFT(nfft, 1);
    sig_hi_res.rangeFFT(oversample*nfft, 1);
 
    // copy original data to device
    sig_lo_res.dataToDevice(slc);

    // init then zero upsampled device data
    sig_hi_res.zeroDeviceData();

    upsampleZ2Z(sig_lo_res, sig_hi_res, slcU);
    
    // Check if the original smaples have the same phase in the signal before and after upsampling
    double max_err = 0.0;
    double err = 0.0;
    for (size_t col = 0; col<width; col++){
        err = std::arg(slc[col] * std::conj(slcU[oversample*col]));
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    double max_err_u = 0.0;
    double err_u;
    double step = 1.0/oversample;
    std::complex<double> cpxData;
    for (size_t col = 0; col<width*oversample; col++){
        double i = col*step;
        double phase = std::sin(10*M_PI*i/(width));
        cpxData = std::complex<double> (std::cos(phase), std::sin(phase));
        err_u = std::arg(cpxData * std::conj(slcU[col]));
        if (std::abs(err_u) > max_err_u){
              max_err_u = std::abs(err_u);
        }
    }    

    ASSERT_LT(max_err, 1.0e-14);
    ASSERT_LT(max_err_u, 1.0e-9);
}
/*
TEST(gpuSignal, ForwardBackwardRangeFloat)
{
    // take a block of data, perform range FFT and then iverse FFT and compare with original data   
    isce::io::Raster inputSlc("../../../../lib/isce/data/warped_envisat.slc.vrt");

    int width = inputSlc.width();
    int length = inputSlc.length();

    // 
    int blockLength = length;

    // reserve memory for a block of data
    std::valarray<std::complex<float>> data(width*blockLength);

    // reserve memory for the spectrum of the block of data
    std::valarray<std::complex<float>> range_spectrum(width*blockLength);

    // reserve memory for a block of data computed from inverse FFT
    std::valarray<std::complex<float>> inverted_data(width*blockLength);

    // a signal object
    gpuSignal<float> sig(CUFFT_C2C);

    // create the plan
    sig.rangeFFT(width, blockLength);
    
    // read a block of data
    inputSlc.getBlock(data, 0, 0, width, blockLength);
   
    // forward fft transform
    sig.forwardC2C(data, range_spectrum);

    // inverse fft transform
    sig.inverseC2C(range_spectrum, inverted_data);

    //normalize the result of inverse fft 
    inverted_data /=width;

    int blockSize = width*blockLength;
    std::complex<float> err(0.0, 0.0);
    bool Test = true;
    double max_err = 0.0;
    for ( size_t i = 0; i < blockSize; ++i ) {
        err = inverted_data[i] - data[i];
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    ASSERT_LT(max_err, 1.0e-4);
}

TEST(gpuSignal, ForwardBackwardAzimuthFloat)
{
    // take a block of data, perform range FFT and then iverse FFT and compare with original data   
    isce::io::Raster inputSlc("../../../../lib/isce/data/warped_envisat.slc.vrt");

    int width = inputSlc.width();
    int length = inputSlc.length();

    // 
    int blockLength = length;

    // reserve memory for a block of data
    std::valarray<std::complex<float>> data(width*blockLength);

    // reserve memory for the spectrum of the block of data
    std::valarray<std::complex<float>> range_spectrum(width*blockLength);

    // reserve memory for a block of data computed from inverse FFT
    std::valarray<std::complex<float>> inverted_data(width*blockLength);

    // a signal object
    gpuSignal<float> sig(CUFFT_C2C);

    // create the plan
    sig.azimuthFFT(width, blockLength);
    
    // read a block of data
    inputSlc.getBlock(data, 0, 0, width, blockLength);
   
    // forward fft transform
    sig.forwardC2C(data, range_spectrum);

    // save outputs

    // inverse fft transform
    sig.inverseC2C(range_spectrum, inverted_data);

    //normalize the result of inverse fft 
    inverted_data /=width;

    int blockSize = width*blockLength;
    std::complex<float> err(0.0, 0.0);
    bool Test = true;
    double max_err = 0.0;
    for ( size_t i = 0; i < blockSize; ++i ) {
        err = inverted_data[i] - data[i];
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    ASSERT_LT(max_err, 1.0e-4);
}

TEST(gpuSignal, nfft)
{
    // This test is same as the previous test but with nfft used for FFT computation instead of number of columns
    isce::io::Raster inputSlc("../../../../lib/isce/data/warped_envisat.slc.vrt");

    int width = inputSlc.width();
    int length = inputSlc.length();
    int blockLength = length;
    
    // fft length for FFT computations 
    int nfft = 512;

    // reserve memory for a block of data
    std::valarray<std::complex<float>> data(nfft*blockLength);

    // reserve memory for the spectrum of the block of data
    std::valarray<std::complex<float>> range_spectrum(nfft*blockLength);

    // reserve memory for a block of data computed from inverse FFT
    std::valarray<std::complex<float>> inverted_data(nfft*blockLength);

    // read a block of data
    std::valarray<std::complex<float>> dataLine(width);
    for (size_t line = 0; line<blockLength; ++line){
        inputSlc.getLine(dataLine, line);
        data[std::slice(line*nfft,width,1)] = dataLine;
    }

    // a signal object
    gpuSignal<float> sig(CUFFT_C2C);

    // create the forward and backward plans
    sig.rangeFFT(nfft, blockLength);

    // forward fft transform
    sig.forwardC2C(data, range_spectrum);

    // inverse fft transform
    sig.inverseC2C(range_spectrum, inverted_data);

    //normalize the result of inverse fft
    inverted_data /= nfft;

    int blockSize = width*blockLength;
    std::complex<float> err(0.0, 0.0);
    bool Test = true;
    double max_err = 0.0;
    for ( size_t i = 0; i < blockSize; ++i ) {
        err = inverted_data[i] - data[i];
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    ASSERT_LT(max_err, 1.0e-4);
}

TEST(gpuSignal, nfftDouble)
{
    int width = 100; //16;
    int length = 1;
    int blockLength = length;

    // fft length for FFT computations
    size_t nfft;

    // instantiate a signal object
    gpuSignal<double> sig(CUFFT_Z2Z);
    sig.nextPowerOfTwo(width, nfft);

    // reserve memory for a block of data with the size of nfft
    std::valarray<std::complex<double>> data(nfft);
    std::valarray<std::complex<double>> spec(nfft);
    std::valarray<std::complex<double>> inverted_data(nfft);

    for (size_t i=0; i<width; ++i){
        double phase = std::sin(10*M_PI*i/width);
        data[i] = std::complex<double> (std::cos(phase), std::sin(phase));
    }

    // create the forward and backward plans
    sig.rangeFFT(nfft, 1);

    // forward fft transform
    sig.forwardZ2Z(data, spec);

    // inverse fft transform
    sig.inverseZ2Z(spec, inverted_data);

    //normalize the result of inverse fft
    inverted_data /= nfft;

    int blockSize = width*blockLength;
    std::complex<float> err(0.0, 0.0);
    bool Test = true;
    double max_err = 0.0;
    for ( size_t i = 0; i < blockSize; ++i ) {
        err = inverted_data[i] - data[i];
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    ASSERT_LT(max_err, 1.0e-4);
}

TEST(gpuSignal, nfftFloat)
{
    int width = 100;
    int length = 1;
    int blockLength = length;

    // fft length for FFT computations
    size_t nfft;

    // instantiate a signal object
    gpuSignal<float> sig(CUFFT_C2C);
    sig.nextPowerOfTwo(width, nfft);

    // reserve memory for a block of data with the size of nfft
    std::valarray<std::complex<float>> data(nfft);
    std::valarray<std::complex<float>> spec(nfft);
    std::valarray<std::complex<float>> dataInv(nfft);

    for (size_t i=0; i<width; ++i){
        double phase = std::sin(10*M_PI*i/width);
        data[i] = std::complex<float> (std::cos(phase), std::sin(phase));
    }

    sig.rangeFFT(nfft, 1);

    sig.forwardC2C(data, spec);
    sig.inverseC2C(spec, dataInv);

    dataInv /=nfft;

    std::complex<float> err(0.0, 0.0);
    bool Test = true;
    double max_err = 0.0;

    for (size_t line = 0; line<blockLength; line++){
        for (size_t col = 0; col<width; col++){
            err = dataInv[line*nfft+col] - data[line*nfft+col];
            if (std::abs(err) > max_err){
                    max_err = std::abs(err);
            }
        }
     }


    // average L2 error as described on 
    // http://www.fftw.org/accuracy/method.html
    std::complex<float> errorL2 ;
    std::complex<float> sumErr;
    std::complex<float> sumB;
    for (size_t line = 0; line<blockLength; line++){
         for (size_t col = 0; col<width; col++){
             sumErr += std::pow((dataInv[line*nfft+col] - data[line*nfft+col]),2);
             sumB += std::pow(dataInv[line*nfft+col], 2);
         }
    }

    errorL2 = std::sqrt(sumErr)/std::sqrt(sumB);
    
    ASSERT_LT(max_err, 1.0e-4);
    ASSERT_LT(std::abs(errorL2), 1.0e-4);
}

TEST(gpuSignal, FFT2D)
{
    int width = 12;
    int length = 10;

    //
    int blockLength = length;

    // reserve memory for a block of data
    std::valarray<std::complex<double>> data(width*blockLength);

    // reserve memory for the spectrum of the block of data
    std::valarray<std::complex<double>> spectrum(width*blockLength);

    // reserve memory for a block of data computed from inverse FFT
    std::valarray<std::complex<double>> invertData(width*blockLength);

    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            data[i*width + j] = std::complex<double> (std::cos(i*j), std::sin(i*j));
        }
    }

    // a signal object
    gpuSignal<double> sig(CUFFT_Z2Z);

    // create plan
    sig.FFT2D(width, blockLength);
  
    sig.forwardZ2Z(data, spectrum);
    sig.inverseZ2Z(spectrum, invertData);
    invertData /=(width*length);

    double max_err = 0.0;
    double err = 0.0;
    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            err = std::abs(data[i*width + j] - invertData[i*width + j]);
            if (err > max_err)
                max_err = err;
        }
    }

    ASSERT_LT(max_err, 1.0e-12);
}

TEST(gpuSignal, rawPointerArrayComplex)
{
    int width = 120;
    int length = 100;

    int blockLength = length;

    // reserve memory for a block of data
    std::complex<double> *data = new std::complex<double>[width*blockLength];
    
    // reserve memory for the spectrum of the block of data
    std::complex<double> *spectrum = new std::complex<double>[width*blockLength];
    
    // reserve memory for a block of data computed from inverse FFT
    std::complex<double> *invertData = new std::complex<double>[width*blockLength];

    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            data[i*width + j] = std::complex<double> (std::cos(i*j), std::sin(i*j));
        }
    }
    
    // a signal object
    gpuSignal<double> sig(CUFFT_Z2Z);

    // ********************************
    // create the forward and backward plans
    sig.FFT2D(width, blockLength);

    // forward and inverse transforms
    sig.forwardZ2Z(data, spectrum);
    sig.inverseZ2Z(spectrum, invertData);

    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            invertData[i*width + j] /=(width*length);
        }
    }

    double max_err_2DFFT = 0.0;
    double err = 0.0;
    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            err = std::abs(data[i*width + j] - invertData[i*width + j]);
            if (err > max_err_2DFFT)
                max_err_2DFFT = err;
        }
    }

    // ********************************
    // Check the error for 2D FFT
    ASSERT_LT(max_err_2DFFT, 1.0e-12);
}

TEST(gpuSignal, realDataFFT)
{
    int width = 120;
    int length = 100;

    int blockLength = length;

    // reserve memory for a block of data
    double *data = new double[width*blockLength];

    // reserve memory for the spectrum of the block of data
    std::complex<double> *spectrum = new std::complex<double>[width*blockLength];

    // reserve memory for a block of data computed from inverse FFT
    double *invertData = new double[width*blockLength];

    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            data[i*width + j] = i+j; 
        }
    }

    // a signal objects
    gpuSignal<double> sig_D2Z(CUFFT_D2Z);
    gpuSignal<double> sig_Z2D(CUFFT_Z2D);

    // make plans
    sig_D2Z.FFT2D(width, blockLength);
    sig_Z2D.FFT2D(width, blockLength);

    // forward and inverse transform
    sig_D2Z.forwardD2Z(data, spectrum);
    sig_Z2D.inverseZ2D(spectrum, invertData);

    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            invertData[i*width + j] /=(width*length);
        }
    }

    double max_err_2DFFT = 0.0;
    double err = 0.0;
    for (size_t i = 0; i< length; ++i){
        for (size_t j = 0; j< width; ++j){
            err = std::abs(data[i*width + j] - invertData[i*width + j]);
            if (err > max_err_2DFFT)
                max_err_2DFFT = err;
        }
    }

    ASSERT_LT(max_err_2DFFT, 1.0e-12);
}

TEST(gpuSignal, upsampleDouble)
{
    int width = 100;
    int length = 1;
    int blockLength = length;

    // fft length for FFT computations
    size_t nfft;

    //sig.nextPowerOfTwo(width, nfft);
    nfft = width;
    // upsampling factor
    int oversample = 2;

    // reserve memory for a block of data with the size of nfft
    std::valarray<std::complex<double>> slc(nfft);
    std::valarray<std::complex<double>> slcU(nfft*oversample);

    for (size_t i=0; i<width; ++i){
        double phase = std::sin(10*M_PI*i/width);
        slc[i] = std::complex<double> (std::cos(phase), std::sin(phase));
    }

    // instantiate a signal object
    gpuSignal<double> sig_input(CUFFT_Z2Z);
    gpuSignal<double> sig_upsample(CUFFT_Z2Z);
 
    sig_input.rangeFFT(nfft, 1);
    sig_upsample.rangeFFT(oversample*nfft, 1);

    upsampleZ2Z(slc, slcU, slc, sig_input, sig_upsample);
    
    // Check if the original smaples have the same phase in the signal before and after upsampling
    double max_err = 0.0;
    double err = 0.0;
    for (size_t col = 0; col<width; col++){
        err = std::arg(slc[col] * std::conj(slcU[oversample*col]));
        if (std::abs(err) > max_err){
            max_err = std::abs(err);
        }
    }

    double max_err_u = 0.0;
    double err_u;
    double step = 1.0/oversample;
    std::complex<double> cpxData;
    for (size_t col = 0; col<width*oversample; col++){
        double i = col*step;
        double phase = std::sin(10*M_PI*i/(width));
        cpxData = std::complex<double> (std::cos(phase), std::sin(phase));
        err_u = std::arg(cpxData * std::conj(slcU[col]));
        if (std::abs(err_u) > max_err_u){
              max_err_u = std::abs(err_u);
        }
    }    

    ASSERT_LT(max_err, 1.0e-14);
    ASSERT_LT(max_err_u, 1.0e-9);
}
*/
int main(int argc, char * argv[]) 
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

// end of file
