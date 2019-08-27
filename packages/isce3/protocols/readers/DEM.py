#-*- coding: utf-8 -*-


# support
import isce3
# superclass
from .Reader import Reader
# my parts
from .. import products


# the reader
class DEM(Reader, family="isce3.readers.dem"):
    """
    Readers of files with digital elevation models
    """


    # user configurable state
    filename = isce3.properties.path()
    filename.doc = "the path to the file with the elevation data"

    # outputs
    dem = products.dem.output()
    dem.doc = "the digital elevation model retrieved from  the file"


    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Provide access to the default reference implementation
        """
        # invoke the foundry and publish the reader
        return isce3.readers.dem()


# end of file
