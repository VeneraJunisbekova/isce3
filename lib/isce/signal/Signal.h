// -*- C++ -*-
// -*- coding: utf-8 -*-
// 
// Author: Heresh Fattahi
// Copyright 2018-
//

#ifndef ISCE_SIGNAL_SIGNAL_H
#define ISCE_SIGNAL_SIGNAL_H

#include <cmath>
#include <valarray>

#include <isce/core/Constants.h>

#include "fftw3cxx.h"

// Declaration
namespace isce {
    namespace signal {
        template<class T>
        class Signal;
    }
}

/** A class to handle 1D FFT in range and azimuth directions 
 *
 */
template<class T> 
class isce::signal::Signal {
    public:
        /** Default constructor. */ 
        Signal() {};

        ~Signal() {};

        /** \brief initiate forward FFTW3 plan for a block of data
         *  input parameters follow FFTW3 interface for fftw_plan_many_dft
         */
        T fftPlanForward(std::valarray<std::complex<T>> &input, 
					std::valarray<std::complex<T>> &output,
            				int rank, int n, int howmany,
            				int inembed, int istride, int idist,
            				int onembed, int ostride, int odist, int sign);


        /** \brief initiate iverse FFTW3 plan for a block of data
         *  input parameters follow FFTW3 interface for fftw_plan_many_dft
         */
        T fftPlanBackward(std::valarray<std::complex<T>> &input,
                                        std::valarray<std::complex<T>> &output,
                                        int rank, int n, int howmany,
                                        int inembed, int istride, int idist,
                                        int onembed, int ostride, int odist, int sign);	

	/** perform forward FFT */
        T forward(std::valarray<std::complex<T>> &input,
                    std::valarray<std::complex<T>> &output);
        
        /** perform forward FFT*/
        T inverse(std::valarray<std::complex<T>> &input,
                    std::valarray<std::complex<T>> &output);

        /** \brief initiate plan for forward FFT in range direction for a block of data
         */
        T forwardRangeFFT(std::valarray<std::complex<T>>& signal, 
					std::valarray<std::complex<T>>& spectrum,
                			int incolumns, int inrows, 
                                        int outcolumns, int outrows);

        /** \brief initiate plan for forward FFT in azimuth direction for a block of data
         */
        T forwardAzimuthFFT(std::valarray<std::complex<T>> &signal,
                                        std::valarray<std::complex<T>> &spectrum,
                                        int incolumns, int inrows, 
                                        int outcolumns, int outrows);

        /** \brief initiate plan for backward FFT in range direction for a block of data
         */
        T inverseRangeFFT(std::valarray<std::complex<T>> &spectrum, 
                                        std::valarray<std::complex<T>> &signal,
                                        int incolumns, int inrows, 
                                        int outcolumns, int outrows);

	/** \brief initiate plan for inverse FFT in azimuth direction for a block of data
         */
        T inverseAzimuthFFT(std::valarray<std::complex<T>> &spectrum,
                                        std::valarray<std::complex<T>> &signal,
                                        int incolumns, int inrows,
                                        int outcolumns, int outrows);

	/** \brief upsampling a block of data in range direction */
        T upsample(std::valarray<std::complex<T>> &signal,
                    std::valarray<std::complex<T>> &signalOversampled,
                    int rows, int nfft, int oversampleFactor);

    private:
        isce::fftw3cxx::plan<T> _plan_fwd;
        isce::fftw3cxx::plan<T> _plan_inv;

};

#endif


