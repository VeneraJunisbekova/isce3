#-*- coding: utf-8 -*-

# support
import nisar


# the flow
class Rdr2Geo(nisar.flow.workflow, family="nisar.workflows.rdr2geo"):
    """
    Convert an SLC from radar to geographic coordinates
    """

    # flow assets
    # the main engine
    rdr2geo = nisar.protocols.factories.rdr2geo()
    rdr2geo.doc = "the SLC converter from radar to geographic coordinates"

    # the necessary factories
    slcReader = nisar.protocols.readers.slc()
    slcReader.doc = "the reader of native SLCs"

    demReader = nisar.protocols.readers.dem()
    demReader.doc = "the digital elevation model reader"

    slcWriter = nisar.protocols.writers.slc()
    slcWriter.doc = "the writer of geocoded SLCs"

    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)

        # unpack
        rdr2geo = self.rdr2geo
        demReader = self.demReader
        slcReader = self.slcReader
        slcWriter = self.slcWriter

        print(f"{self}:")
        print(f"    rdr2geo: {self.rdr2geo}")
        print(f"    demReader: {self.demReader}")
        print(f"    slcReader: {self.slcReader}")
        print(f"    slcWriter: {self.slcWriter}")

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
