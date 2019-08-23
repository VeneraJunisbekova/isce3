#-*- coding: utf-8 -*-


# support
import isce3


# the product
class DEM(isce3.flow.product,
          family="isce3.products.dem.dem", implements=isce3.protocols.products.dem):
    """
    A digital elevation model
    """


# end of file
