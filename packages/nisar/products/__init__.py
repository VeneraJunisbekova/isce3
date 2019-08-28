# -*- coding: utf-8 -*-


# support
import nisar


# product foundries
@nisar.foundry(implements=nisar.protocols.products.slc, tip="the NISAR SLC data product")
def slc():
    """
    The NISAR standard SLC product
    """
    # load the factory
    from .SLC import SLC
    # and publish it
    return SLC


# end of file
