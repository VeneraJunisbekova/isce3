# -*- coding: utf-8 -*-


# support
import nisar
# superclass
from .HDF5 import HDF5


# reader for HDF5 files with NISAR SLC
class SLC(HDF5, family='nisar.readers.slc.slc', implements=nisar.protocols.readers.slc):
    """
    Reader of SLCs from NISAR compliant HDF5 files
    """


    # output
    slc = nisar.protocols.products.slc.output()
    slc.default = nisar.products.slc() # switch the default to the NISAR product
    slc.doc = "the SLC product extracted by this reader"


# end of file
