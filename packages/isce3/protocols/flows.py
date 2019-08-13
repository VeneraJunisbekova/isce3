#-*- coding: utf-8 -*-

# get the package
import isce3


# here, we just redefine the protocols from {pyre.flow} so we can tweak the family names

# the product protocol
class specification(isce3.flow.specification, family="isce3.products"):
    """
    Obligations for products
    """


# the factory protocol
class producer(isce3.flow.producer, family="isce3.factories"):
    """
    Obligations for factories
    """


# the workflow protocol
class flow(isce3.flow.flow, family="isce3.workflows"):
    """
    Obligations for workflows
    """


# end of file
