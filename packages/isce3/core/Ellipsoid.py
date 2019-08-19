#-*- coding: utf-8 -*-

# the package
import isce3
# the isceextension library
import isce3.extensions.isceextension as isceextension

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
    semi_major_axis.const = NotImplemented

    eccentricity_squared = isce3.properties.float()
    eccentricity_squared.default = 0.0066943799901
    eccentricity_squared.doc = "the ellipsoid eccentricity squared"
    eccentricity_squared.const = NotImplemented

    capi_or_cython = isce3.properties.str()
    capi_or_cython.default = "cython"
    capi_or_cython.doc = "choose between using the 'capi' extension or the 'cython' extension"

    # public data
    @property
    def a(self):
        """
        The ellipsoid semi-minor axis
        """
        #a = isce3.libisce.ellipsoid_semiMajor(self.ellipsoid)
        a = self.ellipsoid.a
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
#        b = isce3.libisce.ellipsoid_semiMinor(self.ellipsoid)
        b = self.ellipsoid.b
        # add the units and return it
        return b * isce3.units.length.meter

    @b.setter
    def b(self, x):
        print('e2 is const: create a new ellipsoid')
        return

    @property
    def e2(self):
        """
        The ellipsoid eccentricity-squared
        """
        # e2 = self.ellipsoid_eccentricitySquared(self.ellipsoid)
        # add the units and return it
        return self.ellipsoid.e2

    @e2.setter
    def e2(self, x):
        print('e2 is const: create a new ellipsoid')
        return

    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # allocate an {isce::core::Ellipsoid}
        print("self.capi_or_cython = {}".format(self.capi_or_cython))
        if self.capi_or_cython == 'capi':
            self.ellipsoid = isce3.libisce.ellipsoid(self.semi_major_axis.value, self.eccentricity_squared)
        else:
            self.ellipsoid = isceextension.pyEllipsoid(self.semi_major_axis.value, self.eccentricity_squared)
        # end-if
        # all done
        return


# end of file
