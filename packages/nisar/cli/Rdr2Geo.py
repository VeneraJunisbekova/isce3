#-*- coding: utf-8 -*-


# support
import nisar


# declaration
class Rdr2Geo(nisar.shells.command, family="nisar.cli.rdr2geo"):
    """
    Convert an SLC from radar to geographic coordinates
    """


    # public state
    flow = nisar.protocols.flows.flow()
    flow.default = nisar.workflows.rdr2geo # by default, make the one named after me...
    flow.doc = "the workflow to execute"


    # configuration information
    @nisar.export(tip="validate and display the workflow configuration")
    def config(self, plexus, **kwds):
        """
        Validate and display configuration information
        """
        # grab a channel
        channel = plexus.info
        # show me
        channel.line(f"{self.pyre_name}")
        # if the flow is non-trivial
        if self.flow is not None:
            # show me
            self.flow.pyre_dump(channel=channel, level=1)
        # flush
        channel.log()
        # all done
        return 0


# end of file
