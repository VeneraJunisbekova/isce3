#-*- coding: utf-8 -*-


# support
import isce3


# the factory
class Geo2Rdr(isce3.flow.factory,
              family="isce3.factories.geo2rdr.geo2rdr",
              implements=isce3.protocols.factories.geo2rdr):
    """
    Compute a transformation from geodetic to radar coordinates for a given SLC
    """


    # inputs
    dem = isce3.protocols.products.dem.input()
    dem.doc = "the SLC that defines the transform"


    slc = isce3.protocols.products.slc.input()
    slc.doc = "the SLC that defines the transform"

    ellipsoid = isce3.protocols.core.ellipsoid.input()
    ellipsoid.doc = "the reference ellipsoid"


# end of file
