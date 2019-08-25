#-*- coding: utf-8 -*-


# support
import isce3
# superclass
from .Reader import Reader


# the reader
class DEM(Reader, family="isce3.readers.dem"):
    """
    Readers of files with digital elevation models
    """


    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Provide access to the default reference implementation
        """
        # invoke the foundry and publish the reader
        return isce3.readers.dem()


# end of file
