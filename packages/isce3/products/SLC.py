#-*- coding: utf-8 -*-


# support
import isce3


# the product
class SLC(isce3.flow.product,
          family="isce3.products.slc", implements=isce3.protocols.products.slc):
    """
    The base SLC product
    """

# end of file
