# -*- coding: utf-8 -*-


# support
import isce3


# the base class for SLC products
class SLC(isce3.products.slc(), family="nisar.products.slc"):
    """
    The base SLC product
    """


# end of file
