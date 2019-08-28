#-*- coding: utf-8 -*-


# support
import isce3


# declaration
class Workflow(isce3.shells.command, family="isce3.cli.workflow"):
    """
    Base class for command panels that invoke workflows
    """


    # public state
    flow = isce3.protocols.flows.flow()
    flow.doc = "the workflow to execute"


    # create a new geo2rdr flow
    @isce3.export(tip="create a new instance of a the workflow")
    def new(self, plexus, **kwds):
        """
        Persist the current flow in a configuration file
        """
        # grab a channel
        channel = plexus.info
        # show me
        channel.log(f"saving '{self.flow.pyre_name}'")
        # do it
        self.flow.pyre_save()
        # all done
        return 0


    # load a persisted flow and display its layout
    @isce3.export(tip="display information about an existing workflow instance")
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
