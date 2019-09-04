#-*- coding: utf-8 -*-


# get the package
import isce3


# protocols for the core objects
class Ellipsoid(isce3.flow.specification, family="isce.core.ellipsoids"):
    """
    Specification of {isce3} compatible geodetic models
    """


    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Provide access to the reference implementation
        """
        # by default, use the WGS84 reference ellipsoid
        return isce3.wgs84


# end of file
