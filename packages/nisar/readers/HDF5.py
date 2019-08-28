# -*- coding: utf-8 -*-


# support
import nisar


# the base reader
class HDF5(nisar.flow.factory):
    """
    Base class for readers that extract NISAR products from HDF5 files
    """


    # user configurable state
    filename = nisar.properties.path()
    filename.doc = "the path to the HDF5 file with the product to extract"



# end of file
