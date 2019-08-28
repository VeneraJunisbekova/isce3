#-*- coding: utf-8 -*-

# support
import isce3


# the flow
class Geo2Rdr(isce3.flow.workflow, family="isce3.workflows.geo2rdr"):
    """
    Compute the transformation from geodetic to radar coordinates for a given SLC
    """

    # flow assets
    # the main engine
    geo2rdr = isce3.protocols.factories.geo2rdr()
    geo2rdr.doc = "the SLC converter from radar to geodetic coordinates"

    # sources of input
    slcReader = isce3.protocols.readers.slc()
    slcReader.doc = "the reader of native SLCs"

    demReader = isce3.protocols.readers.dem()
    demReader.doc = "the digital elevation model reader"


    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)

        # unpack
        geo2rdr = self.geo2rdr
        demReader = self.demReader
        slcReader = self.slcReader

        # bind
        geo2rdr.dem = self.demReader.dem
        geo2rdr.slc = self.slcReader.slc

        # all done
        return


# end of file
