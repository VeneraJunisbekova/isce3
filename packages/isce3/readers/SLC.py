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


    # user configurable state
    filename = isce3.properties.path()
    filename.doc = "the path to the SLC file"

    # outputs
    slc = isce3.protocols.products.slc.output()
    slc.doc = "the SLC product retrieved from the file"


# end of file
