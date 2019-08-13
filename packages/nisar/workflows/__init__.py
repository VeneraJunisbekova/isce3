#-*- coding: utf-8 -*-

# support
import nisar


# the rdr2geo workflow
@nisar.foundry(tip="geocode an SLC", implements=nisar.protocols.flows.flow)
def rdr2geo():
    # grab the flow
    from .Rdr2Geo import Rdr2Geo
    # steal its docstring
    __doc__ = Rdr2Geo.__doc__
    # and publish it
    return Rdr2Geo


# end of file
