#-*- coding: utf-8 -*-


# get the package
import isce3


# command foundries
# info about the app
@isce3.foundry(implements=isce3.shells.action, tip="display information about this app")
def about():
    """
    Display human readable information about the app
    """
    # load the command
    from .About import About
    # and publish it
    return About


# information about the layout of the isce3 package
@isce3.foundry(implements=isce3.shells.action, tip="information about the layout of {isce3}")
def config():
    """
    Display configuration information about the {isce3} package
    """
    # load the command
    from .Config import Config
    # and publish it
    return Config


# easy access to specific workflows
@isce3.foundry(implements=isce3.shells.action,
               tip="compute a transformation from geodetic to radar coordinates for a given SLC")
def geo2rdr():
    """
    Invoke the {geo2rd} workflow to compute the transformation from geodetic coordinates to
    radar coordinates for a given SLC
    """
    # load the command
    from .Geo2Rdr import Geo2Rdr
    # and publish it
    return Geo2Rdr


@isce3.foundry(implements=isce3.shells.action,
               tip="compute a transformation from radar to geodetic coordinates for a given SLC")
def rdr2geo():
    """
    Invoke the {rdr2geo} workflow to compute the transformation from radar coordinates to
    geodetic coordinates for a given SLC
    """
    # load the command
    from .Rdr2Geo import Rdr2Geo
    # and publish it
    return Rdr2Geo


# support
@isce3.foundry(implements=isce3.shells.action)
def complete():
    """
    Support for auto-completion
    """
    # load the command
    from .Complete import Complete
    # and publish it
    return Complete


# end of file
