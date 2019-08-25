#-*- coding: utf-8 -*-


# get the package
import isce3


# the factory protocol
class producer(isce3.flow.producer, family="isce3.factories"):
    """
    Obligations for factories
    """


# geometric transformations between radar and geodetic coordinates
class rdr2geo(producer, family="isce3.factories.rdr2geo"):
    """
    Compute a transformation from radar to geodetic coordinates for a given SLC
    """

    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Supply the reference implementation of the {rdr2geo} factory
        """
        # get the {isce3} reference implementation and publish it
        return isce3.factories.rdr2geo()


class geo2rdr(producer, family="isce3.factories.geo2rdr"):
    """
    Compute a transformation from geodetic to radar coordinates for a given SLC
    """

    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Supply the reference implementation of the {geo2rdr} factory
        """
        # get the {isce3} reference implementation and publish it
        return isce3.factories.geo2rdr()



# end of file
