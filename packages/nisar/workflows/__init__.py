#-*- coding: utf-8 -*-

# support
import nisar


# the geo2rdr workflow
@nisar.foundry(tip="compute a transformation from geodetic to radar coordinates given an SLC",
               implements=nisar.protocols.flows.flow)
def geo2rdr():
    """
    Compute the transformation from geodetic to radar coordinates for a given NISAR compliant
    SLC product
    """
    # grab the flow
    from .Geo2Rdr import Geo2Rdr
    # and publish it
    return Geo2Rdr


# the rdr2geo workflow
@nisar.foundry(tip="compute a transformation from radar to geodetic coordinates given an SLC",
               implements=nisar.protocols.flows.flow)
def rdr2geo():
    """
    Compute the transformation from radar to geodetic coordinates for a given NISAR compliant
    SLC product
    """
    # grab the flow
    from .Rdr2Geo import Rdr2Geo
    # and publish it
    return Rdr2Geo


# end of file
