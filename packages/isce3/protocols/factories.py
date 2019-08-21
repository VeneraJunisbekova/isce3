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
    Convert an SLC from radar to geographic coordinates
    """


class geo2rdr(producer, family="isce3.factories.geo2rdr"):
    """
    Convert an SLC from geographic to radar coordinates
    """


# end of file
