#-*- coding: utf-8 -*-

# the package
import isce3


# declaration
class Ellipsoid(isce3.flow.product,
                family="isce3.ellipsoid", implements=isce3.protocols.core.ellipsoid):
    """
    The reference implementation of a simple geodetic ellipsoid
    """


    # user configurable state
    a = isce3.properties.dimensional()
    a.default = 6378.1370 * isce3.units.length.km
    a.doc = "the ellipsoid semi-major axis"
    a.const = NotImplemented

    e2 = isce3.properties.float()
    e2.default = 0.0066943799901
    e2.doc = "the ellipsoid eccentricity squared"
    e2.const = NotImplemented


    # public data
    @property
    def b(self):
        """
        The ellipsoid semi-minor axis
       """
        # get the value, expected in meters
        b = self.ellipsoid.b
        # decorate with units and return it
        return b * isce3.units.length.meter


    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # ask the isce extension for an instance
        self.ellipsoid = isce3.libisce.pyEllipsoid(self.a.value, self.e2)
        # all done
        return


# end of file
