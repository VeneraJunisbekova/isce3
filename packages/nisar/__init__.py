#-*- coding: utf-8 -*-

# import and publish pyre symbols
from isce3 import (
    # protocols, components, traits, and their infrastructure
    schemata, constraints, properties, protocol, component, foundry,
    # component interface decorators
    export, provides,
    # the manager of the pyre runtime
    executive,
    # multidimensional containers
    grid,
    # concurrency
    nexus,
    # workflows
    flow,
    # miscellaneous
    tracking, units, weaver,
    )


# bootstrap
package = executive.registerPackage(name='nisar', file=__file__)
# save the geography
home, prefix, defaults = package.layout()


# publish the local modules
from . import (
    meta,        # package meta-data
    shells,      # application support
)


# administrative
def copyright():
    """
    Print the nisar copyright note
    """
    return print(meta.header)


def license():
    """
    Print the nisar license
    """
    # print it
    return print(meta.license)


def version():
    """
    Return the nisar version
    """
    return meta.version


def credits():
    """
    Print the acknowledgments
    """
    # print it
    return print(meta.acknowledgments)


# end of file
