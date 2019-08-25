#-*- coding: utf-8 -*-


# support
import isce3
import nisar


# extend the {isce3} command by the same name
class Rdr2Geo(isce3.cli.rdr2geo(), family="nisar.cli.rdr2geo"):
    """
    Invoke the {rdr2geo} workflow to compute the transformation from radar to geodetic
    coordinates for a given NISAR compliant SLC product
    """


    # public state
    # redefine {flow} so we can adjust the default
    flow = nisar.protocols.flows.flow()
    flow.default = nisar.workflows.rdr2geo # by default, make the one named after me...
    flow.doc = "the workflow to execute"


# end of file
