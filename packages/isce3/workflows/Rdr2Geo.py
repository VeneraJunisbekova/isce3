#-*- coding: utf-8 -*-

# support
import isce3


# the flow
class Rdr2Geo(isce3.flow.workflow, family="isce3.workflows.rdr2geo"):
    """
    Compute the transformation from radar coordinates to geodetic coordinates for a given SLC
    """

    # flow assets
    # the main engine
    rdr2geo = isce3.protocols.factories.rdr2geo()
    rdr2geo.doc = "the SLC converter from radar to geodetic coordinates"

    # the necessary factories
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

        print(f"{self}:")
        print(f"    rdr2geo: {self.rdr2geo}")
        print(f"    demReader: {self.demReader}")
        print(f"    slcReader: {self.slcReader}")

        # all done
        return
        # bind the parts together to make the flow
        # connect the geo2rdr inputs
        rdr2geo.radarSLC = slcReader.slc
        rdr2geo.dem = demReader.dem
        # and its outputs
        slcWriter.slc = rdr2geo.geocodedSLC

        # all done
        return


# end of file
