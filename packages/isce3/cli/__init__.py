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


# end of file
