#-*- coding: utf-8 -*-


# support
import isce3


# the product
class SLC(isce3.flow.product,
          family="isce3.products.slc.slc", implements=isce3.protocols.products.slc):
    """
    The base SLC product
    """


    # product meta-data
    samples = isce3.properties.int()
    samples.doc = "the number of samples in a line"

    lines = isce3.properties.int()
    lines.doc = "the number of acquisition lines"


# end of file
