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


    # create a new rdr2geo flow
    @nisar.export(tip="create a new instance of an rdr2geo flow")
    def new(self, plexus, **kwds):
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


    # load a persisted flow and display its layout
    @nisar.export(tip="display information about an existing rdr2geo flow instance")
    def info(self, plexus, **kwds):
        """
        Load a flow from a configuration file and display its layout
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
