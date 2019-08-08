# -*- coding: utf-8 -*-

# super class
from .HDF5 import HDF5

# slc hdf5 reader
class SLC(HDF5, family='nisar.readers.slc'):
    '''
    Class for parsing NISAR SLC products into isce structures.
    '''

    # validation tag to ensure correct product type
    productValidationType = "SLC"

# end-of-file
