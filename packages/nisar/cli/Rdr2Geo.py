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


    # load a persisted flow
    @nisar.export(tip="persist the current flow")
    def load(self, plexus, **kwds):
        """
        Load a flow from a configuration file
        """
        # grab a channel
        channel = plexus.info
        # show me
        channel.log(f"loading '{self.flow.pyre_name}'")
        # show me
        self.flow.pyre_dump(channel=channel, level=1)
        # all done
        return 0


    # persist a flow
    @nisar.export(tip="persist the current flow")
    def save(self, plexus, **kwds):
        """
        Persist the current flow in a configuration file
        """
        # grab a channel
        channel = plexus.info
        # show me
        channel.log(f"saving '{self.flow.pyre_name}'")
        # do it
        self.flow.save()
        # all done
        return 0


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
