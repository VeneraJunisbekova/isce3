# -*- coding: utf-8 -*-
#
# Authors: ?, Liang Yu
# Copyright 2019-
#

import os
import gdal
import pyre
from ..Base import Base

class SLC(Base, family='nisar.productreader.slc'):
    '''
    Class for parsing NISAR SLC products into isce structures.
    '''
   
    productValidationType = pyre.properties.str(default='SLC')
    productValidationType.doc = 'Validation tag to ensure correct product type'

    def __init__(self, **kwds):
        '''
        Constructor to initialize product with HDF5 file.
        '''

        ###Read base product information like Identification
        super().__init__(**kwds) 

    def getGdalSlcDataset(self, frequency, polarization):
        '''
        Return SLC as GDAL dataset
        '''
        # TODO add error check for path and file
        # construct path to datast
        ds_path = os.path.join(self.SwathPath, 'frequency{0}'.format(frequency), polarization)

        # construct string to feed to GDAL
        gdal_path = 'HDF5:"{}":/{}'.format(self.filename, ds_path)

        # get GDAL dataset
        ds = gdal.Open(gdal_path, gdal.GA_ReadOnly)

        return ds

# end of file
