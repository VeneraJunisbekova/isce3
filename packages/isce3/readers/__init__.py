#-*- coding: utf-8 -*-


# support
import isce3


# the reader of digital elevation models
@isce3.foundry(implements=isce3.protocols.readers.dem,
               tip="a reader of digital elevation models in standard isce3 format")
def dem():
    """
    Access the reference implementation of a digital elevation model reader
    """
    # pull the factory
    from .DEM import DEM
    # and publish it
    return DEM


# the reader of SLCs
@isce3.foundry(implements=isce3.protocols.readers.slc,
               tip="a reader of SLC products in standard isce3 format")
def slc():
    """
    Access the reference implementation of an SLC reader
    """
    # pull the factory
    from .SLC import SLC
    # and publish it
    return SLC


# end of file
