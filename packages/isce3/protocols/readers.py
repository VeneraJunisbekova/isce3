#-*- coding: utf-8 -*-


# the base protocol
from .factories import producer


# the readers
class reader(producer, family="isce3.readers"):
    """
    Obligations for readers of the various supported file formats
    """


class slc(reader, family="isce3.readers.slc"):
    """
    Readers of files that encode SLC
    """


class dem(reader, family="isce3.readers.dem"):
    """
    Readers of files with digital elevation models
    """


# end of file
