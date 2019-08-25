#-*- coding: utf-8 -*-


# support
import isce3
# superclass
from .Reader import Reader


# the reader
class SLC(Reader, family="isce3.readers.slc.slc", implements=isce3.protocols.readers.slc):
    """
    A reader of the standard isce3 encoding of SLCs
    """


# end of file
