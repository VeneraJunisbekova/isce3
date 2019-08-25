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
        geo2rdr = self.geo2rdr
        demReader = self.demReader
        slcReader = self.slcReader

        print(f"{self}:")
        print(f"    geo2rdr: {self.geo2rdr}")
        print(f"    demReader: {self.demReader}")
        print(f"    slcReader: {self.slcReader}")

        # all done
        return
        # bind the parts together to make the flow
        # connect the geo2rdr inputs
        geo2rdr.radarSLC = slcReader.slc
        geo2rdr.dem = demReader.dem

        # all done
        return


# end of file
