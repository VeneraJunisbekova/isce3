#-*- coding: utf-8 -*-


# support
import isce3
# superclass
from .Reader import Reader
# my parts
from .. import products

# the SLC reader
class SLC(Reader, family="isce3.readers.slc"):
    """
    Readers of files that encode SLC
    """


    # required state
    filename = isce3.properties.path()
    filename.doc = "the path to the SLC file"

    # outputs
    slc = products.slc.output()
    slc.doc = "the SLC product retrieved from the file"


    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Provide access to the default reference implementation
        """
        # invoke the foundry and publish the reader
        return isce3.readers.slc()


# end of file
