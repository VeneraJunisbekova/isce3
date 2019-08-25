#-*- coding: utf-8 -*-


# support
import isce3


# transformation between radar and geodetic coordinates
@isce3.foundry(implements=isce3.protocols.factories.rdr2geo,
               tip="compute the transformation from radar to geodetic coordinates")
def rdr2geo():
    """
    Compute the transformation from radar to geodetic coordinates for a given SLC
    """
    # pull the factory
    from .Rdr2Geo import Rdr2Geo
    # and publish it
    return Rdr2Geo


@isce3.foundry(implements=isce3.protocols.factories.geo2rdr,
               tip="compute the transformation from radar to geodetic coordinates")
def geo2rdr():
    """
    Compute the transformation from geodetic to radar coordinates for a given SLC
    """
    # pull the factory
    from .Geo2Rdr import Geo2Rdr
    # and publish it
    return Geo2Rdr


# end of file
