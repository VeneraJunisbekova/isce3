#-*- coding: utf-8 -*-


# support
import isce3
# superclass
from .Reader import Reader


# the reader
class DEM(Reader, family="isce3.readers.dem.dem", implements=isce3.protocols.readers.dem):
    """
    A reader of the standard isce3 encoding of digital elevation models
    """


    # user configurable state
    filename = isce3.properties.path()
    filename.doc = "the path to the file with the elevation data"

    # outputs
    dem = isce3.protocols.products.dem.output()
    dem.doc = "the digital elevation model retrieved from  the file"


# end of file
