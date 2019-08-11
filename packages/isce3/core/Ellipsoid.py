#-*- coding: utf-8 -*-

# the package
import isce3


# declaration
class Ellipsoid(isce3.component,
                family="isce3.ellipsoid", implements=isce3.protocols.core.ellipsoid):
    """
    The reference implementation of a simple reference geodetic ellipsoid
    """


    # user configurable state
    a = isce3.properties.dimensional()
    a.default = 6378.1370 * isce3.units.length.km
    a.doc = "the ellipsoid semi-major axis"

    e2 = isce3.properties.float()
    e2.default = .0066943799901
    e2.doc = "the ellipsoid eccentricity squared"


    # public data
    @property
    def b(self):
        """
        The ellipsoid semi-minor axis
        """
        # get the value, expected in meters
        self._b = isce3.libisce.ellipsoid_semiMinor(self.ellipsoid)
        # add the units and return it
        return self._b * isce3.units.length.meter


    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # allocate an {isce::core::Ellipsoid}
        self.ellipsoid = isce3.libisce.ellipsoid(self.a.value, self.e2)
        # all done
        return


# end of file
