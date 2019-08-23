#-*- coding: utf-8 -*-


# support
import isce3


# extend the {isce3} command by the same name
class Geo2Rdr(isce3.cli.geo2rdr(), family="nisar.cli.geo2rdr"):
    """
    Invoke the {geo2rdr} workflow to compute the transformation from geodetic coordinates to
    radar coordinates for a given NISAR compliant SLC product
    """


# end of file
