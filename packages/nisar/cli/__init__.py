#-*- coding: utf-8 -*-


# support
import nisar


# command foundries
# info about the app
@nisar.foundry(implements=nisar.shells.action, tip="display information about this app")
def about():
    # load the command
    from .About import About
    # steal its docstring
    __doc__ = About.__doc__
    # and publish it
    return About


# information about the layout of the nisar package
@nisar.foundry(implements=nisar.shells.action, tip="information about the layout of {nisar}")
def config():
    # load the command
    from .Config import Config
    # steal its docstring
    __doc__ = Config.__doc__
    # and publish it
    return Config


# easy access to specific workflows
@nisar.foundry(implements=nisar.shells.action,
               tip="compute a transformation from geodetic to radar coordinates given a NISAR SLC")
def geo2rdr():
    # load the command
    from .Geo2Rdr import Geo2Rdr
    # steal its docstring
    __doc__ = Geo2Rdr.__doc__
    # and publish it
    return Geo2Rdr


@nisar.foundry(implements=nisar.shells.action,
               tip="compute a transformation from radar to geodetic coordinates given a NISAR SLC")
def rdr2geo():
    # load the command
    from .Rdr2Geo import Rdr2Geo
    # steal its docstring
    __doc__ = Rdr2Geo.__doc__
    # and publish it
    return Rdr2Geo


# end of file
