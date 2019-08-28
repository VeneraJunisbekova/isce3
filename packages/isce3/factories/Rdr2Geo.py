#-*- coding: utf-8 -*-


# support
import isce3


# the factory
class Rdr2Geo(isce3.flow.factory,
              family="isce3.factories.rdr2geo.rdr2geo",
              implements=isce3.protocols.factories.rdr2geo):
    """
    Compute a transformation from radar to geodetic coordinates for a given SLC
    """


    # inputs
    dem = isce3.protocols.products.dem.input()
    dem.doc = "the SLC that defines the transform"


    slc = isce3.protocols.products.slc.input()
    slc.doc = "the SLC that defines the transform"


# end of file
