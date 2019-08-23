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
    reference = 'resamp_ref.h5'
    frequency = 'A'
    polarization = 'HH'
    offsetdir = 'offsets'
    outdir = 'resamp'

def test_resamp_no_reference():
    '''
    run resample SLC without reference SLC
    current success = no crash
    '''
    opts = resamp_opts()
    opts.reference = ''
    resampSlc.main(opts)

if __name__ == '__main__':
    test_resamp_no_reference()

# end of file
