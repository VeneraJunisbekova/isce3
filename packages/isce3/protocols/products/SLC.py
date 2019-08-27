#-*- coding: utf-8 -*-


# get the package
import isce3
# superclass
from .Specification import Specification


# the SLC specification
class SLC(Specification, family="isce3.products.slc"):
    """
    The SLC product specification
    """


    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Provide access to the reference implementation
        """
        # invoke the foundry and publish the product
        return isce3.products.slc()


# end of file
