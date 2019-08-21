#-*- coding: utf-8 -*-


# support
import isce3


# product foundries
@isce3.foundry(implements=isce3.protocols.products.slc,
               tip="the base SLC product")
def slc():
    """
    The base SLC product
    """
    # load the product
    from .SLC import SLC
    # and publish it
    return SLC


@isce3.foundry(implements=isce3.protocols.products.dem,
               tip="a digital elevation model")
def dem():
    """
    A digital elevation model
    """
    # load the product
    from .DEM import DEM
    # and publish it
    return DEM


# end of file
