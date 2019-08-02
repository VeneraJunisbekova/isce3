#-*- coding: utf-8 -*-


# get the package
import isce3


# command foundries
# info about the app
@isce3.foundry(implements=isce3.shells.action, tip="display information about this app")
def about():
    # load the command
    from .About import About
    # steal its docstring
    __doc__ = About.__doc__
    # and publish it
    return About


# information about the layout of the isce3 package
@isce3.foundry(implements=isce3.shells.action, tip="information about the layout of {isce3}")
def config():
    # load the command
    from .Config import Config
    # steal its docstring
    __doc__ = Config.__doc__
    # and publish it
    return Config


# easy access to specific workflows
@isce3.foundry(implements=isce3.shells.action,
               tip="convert an SLC from geographic to radar coordinates")
def geo2rdr():
    # load the command
    from .Geo2Rdr import Geo2Rdr
    # steal its docstring
    __doc__ = Geo2Rdr.__doc__
    # and publish it
    return Geo2Rdr


@isce3.foundry(implements=isce3.shells.action,
               tip="convert an SLC from radar to geographic coordinates")
def rdr2geo():
    # load the command
    from .Rdr2Geo import Rdr2Geo
    # steal its docstring
    __doc__ = Rdr2Geo.__doc__
    # and publish it
    return Rdr2Geo


# end of file
