# -*- coding: utf-8 -*-


# support
import nisar


# the reader of SLCs
@nisar.foundry(implements=nisar.protocols.readers.slc,
               tip="a reader of SLC products in standard NISAR format")
def slc():
    """
    Access the reference implementation of a reader for a NISAR SLC
    """
    # pull the factory
    from .SLC import SLC
    # and publish it
    return SLC


# end of file
