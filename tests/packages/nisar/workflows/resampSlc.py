#!/usr/bin/env python3
#
# Author: Liang Yu
# Copyright 2019-

from nisar.workflows import resampSlc

class resamp_opts:
    '''
    class to emulate argparse terminal input
    member values set to test basic functionality
    values can be adjusted to meet test requirements
    '''
    product = 'resamp_prod.h5'
    frequency = 'A'
    polarization = 'HH'
    offsetdir = 'offsets'
    outdir = 'resamp'

def test_resamp():
    '''
    run resample SLC
    current success = no crash
    '''
    opts = resamp_opts()
    resampSlc.main(opts)

if __name__ == '__main__':
    test_resamp()

# end of file
