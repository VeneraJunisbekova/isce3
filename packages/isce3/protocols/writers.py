#-*- coding: utf-8 -*-


# the base protocol
from .factories import producer


# the writers
class writer(producer, family="isce3.writers"):
    """
    Obligations for writers of the various supported file formats
    """


class slc(writer, family="isce3.writers.slc"):
    """
    Writers of files that encode SLC
    """


class dem(writer, family="isce3.writers.dem"):
    """
    Writers of files with digital elevation models
    """


# end of file
