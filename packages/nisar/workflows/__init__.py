#-*- coding: utf-8 -*-

# support
import nisar


# the rdr2geo workflow
@nisar.foundry(tip="compute a transformation from radar to geodetic coordinates given an SLC",
               implements=nisar.protocols.flows.flow)
def rdr2geo():
    """
    Compute the transformation from radar coordinates to geodetic coordinates for a given NISAR
    compliant SLC product
    """
    # grab the flow
    from .Rdr2Geo import Rdr2Geo
    # and publish it
    return Rdr2Geo


# end of file
