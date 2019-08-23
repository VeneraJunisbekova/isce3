#-*- coding: utf-8 -*-


# support
import isce3


# declaration
class Rdr2Geo(isce3.shells.command, family="isce3.cli.rdr2geo"):
    """
    Invoke the {rdr2geo} workflow to compute the transformation from radar coordinates to
    geodetic coordinates for a given SLC
    """


    # public state
    flow = isce3.protocols.flows.flow()
    flow.default = isce3.workflows.rdr2geo # by default, make the one named after me...
    flow.doc = "the workflow to execute"


    # create a new rdr2geo flow
    @isce3.export(tip="create a new instance of an rdr2geo flow")
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
    @isce3.export(tip="display information about an existing rdr2geo flow instance")
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
