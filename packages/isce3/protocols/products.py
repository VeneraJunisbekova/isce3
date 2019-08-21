#-*- coding: utf-8 -*-


# get the package
import isce3


# the product protocol
class specification(isce3.flow.specification, family="isce3.products"):
    """
    Obligations for products
    """


# the SLC specification
class slc(specification, family="isce3.products.slc"):
    """
    The SLC product specification
    """


# digital elevation models
class dem(specification, family="isce3.products.dem"):
    """
    The DEM product specification
    """


# end of file
