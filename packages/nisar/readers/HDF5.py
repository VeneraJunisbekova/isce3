# -*- coding: utf-8 -*-


# externals
import h5py
# support
import nisar


# the base reader
class HDF5(nisar.flow.factory):
    """
    Base class for readers that extract NISAR products from HDF5 files
    """


    # user configurable state
    filename = nisar.properties.path()
    filename.doc = "the path to the HDF5 file with the product to extract"


    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)

        # if we have a valid filename
        if self.filename:
            # open the HDF5 file and access the top level group
            self._root = h5py.File(self.filename, mode="r")

        # all done
        return


    # implementation details
    # private data
    _root = None  # the top level group of the HDF5 file


    # constants
    # the file layout
    LSAR = nisar.primitives.path("science/LSAR")
    IDENTIFICATION = LSAR / "identification"


# end of file
