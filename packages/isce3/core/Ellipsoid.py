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
    semi_major_axis = isce3.properties.dimensional()
    semi_major_axis.default = 6378.1370 * isce3.units.length.km
    semi_major_axis.doc = "the ellipsoid semi-major axis"

    eccentricity_squared = isce3.properties.float()
    eccentricity_squared.default = .0066943799901
    eccentricity_squared.doc = "the ellipsoid eccentricity squared"


    # public data
    @property
    def a(self):
        """
        The ellipsoid semi-minor axis
        """
        a = isce3.libisce.ellipsoid_semiMajor(self.ellipsoid)
        # return the value
        return a * isce3.units.length.meter

    @a.setter
    def a(self, x):
        print('a is const: create a new ellipsoid')
        return

    @property
    def b(self):
        """
        The ellipsoid semi-minor axis
        """
        # get the value, expected in meters
        b = isce3.libisce.ellipsoid_semiMinor(self.ellipsoid)
        # add the units and return it
        return b * isce3.units.length.meter

    @b.setter
    def b(self, x):
        print('e2 is const: create a new ellipsoid')
        return

    @property
    def e2(self):
        """
        The ellipsoid semi-minor axis
        """
        e2 = isce3.libisce.ellipsoid_eccentricitySquared(self.ellipsoid)
        # add the units and return it
        return self.eccentricity_squared

    @e2.setter
    def e2(self, x):
        print('e2 is const: create a new ellipsoid')
        return

    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # allocate an {isce::core::Ellipsoid}
        self.ellipsoid = isce3.libisce.ellipsoid(self.semi_major_axis.value, self.eccentricity_squared)
        # all done
        return


# end of file
