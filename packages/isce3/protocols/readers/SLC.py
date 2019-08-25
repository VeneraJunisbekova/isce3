#-*- coding: utf-8 -*-


# support
import isce3
# superclass
from .Reader import Reader


# the SLC reader
class SLC(Reader, family="isce3.readers.slc"):
    """
    Readers of files that encode SLC
    """


    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Provide access to the default reference implementation
        """
        # invoke the foundry and publish the reader
        return isce3.readers.slc()


# end of file
