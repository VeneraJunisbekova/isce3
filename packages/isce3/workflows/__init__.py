#-*- coding: utf-8 -*-


# support
import isce3


# the rdr2geo workflow foundry
@isce3.foundry(tip="geocode an SLC", implements=isce3.protocols.flows.flow)
def rdr2geo():
    """
    Compute the transformation from radar coordinates to geodetic coordinates for a given SLC
    """
    # grab the flow
    from .Rdr2Geo import Rdr2Geo
    # and publish it
    return Rdr2Geo


# end of file
