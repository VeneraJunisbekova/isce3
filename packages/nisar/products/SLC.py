# -*- coding: utf-8 -*-


# support
import isce3
import nisar


# the NISAR SLC data product extends the one from isce3
class SLC(isce3.products.slc(), family="nisar.products.slc.slc"):
    """
    The NISAR SLC data product
    """


# end of file
