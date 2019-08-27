#-*- coding: utf-8 -*-

# support
import isce3


# the flow
class Rdr2Geo(isce3.flow.workflow, family="isce3.workflows.rdr2geo"):
    """
    Compute the transformation from radar to geodetic coordinates for a given SLC
    """

    # flow assets
    # the main engine
    rdr2geo = isce3.protocols.factories.rdr2geo()
    rdr2geo.doc = "the SLC converter from radar to geodetic coordinates"

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
        rdr2geo = self.rdr2geo
        demReader = self.demReader
        slcReader = self.slcReader

        # bind
        rdr2geo.dem = demReader.dem
        rdr2geo.slc = slcReader.slc

        # all done
        return


# end of file
