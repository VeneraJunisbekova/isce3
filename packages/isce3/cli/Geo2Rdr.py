#-*- coding: utf-8 -*-


# support
import isce3


# declaration
class Geo2Rdr(isce3.shells.command, family="isce3.cli.geo2rdr"):
    """
    Invoke the {geo2rd} workflow to compute the transformation from geodetic coordinates to
    radar coordinates for a given SLC
    """


# end of file
