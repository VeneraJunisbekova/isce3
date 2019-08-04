#-*- coding: utf-8 -*-


# get the package
import isce3


# factories for core components
def newEllipsoid(**kwds):
    """
    Create a new ellipsoid
    """
    # pull the implementation
    from .Ellipsoid import Ellipsoid
    # make one and return it
    return Ellipsoid(**kwds)


# foundries for core components
@isce3.foundry(implements=isce3.protocols.core.ellipsoid,
               tip="the reference implementation of an ellipsoidal gravitational model")
def ellipsoid():
    # pull the implementation
    from .Ellipsoid import Ellipsoid
    # steal its docstring
    __doc__ = Ellipsoid.__doc__
    # and publish it
    return Ellipsoid


# end of file
