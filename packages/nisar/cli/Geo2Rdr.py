#-*- coding: utf-8 -*-


# support
import isce3
import nisar


# extend the {isce3} command by the same name
class Geo2Rdr(isce3.cli.geo2rdr(), family="nisar.cli.geo2rdr"):
    """
    Invoke the {geo2rdr} workflow to compute the transformation from geodetic to radar
    coordinates for a given NISAR compliant SLC product
    """


    # public state
    # redefine {flow} so we can adjust the default
    flow = nisar.protocols.flows.flow()
    flow.default = nisar.workflows.geo2rdr # by default, make the one named after me...
    flow.doc = "the workflow to execute"


# end of file
