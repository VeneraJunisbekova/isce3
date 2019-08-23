#-*- coding: utf-8 -*-


# get the package
import isce3


# the factory protocol
class producer(isce3.flow.producer, family="isce3.factories"):
    """
    Obligations for factories
    """


# the factories of various types of SLC
class rdr2geo(producer, family="isce3.factories.rdr2geo"):
    """
    Compute a transformation from radar to geodetic coordinates for a given SLC
    """


class geo2rdr(producer, family="isce3.factories.geo2rdr"):
    """
    Compute a transformation from geodetic to radar coordinates for a given SLC
    """


# end of file
