#-*- coding: utf-8 -*-

# support
import isce3
import nisar


# the {rdr2geo} workflow with {nisar} specific defaults
class Rdr2Geo(isce3.workflows.rdr2geo(), family="nisar.workflows.rdr2geo"):
    """
    Compute the transformation from radar to geodetic coordinates for a given NISAR compliant
    SLC product
    """


    # override the SLC reader to install the {nisar} specific defaults
    slcReader = nisar.protocols.readers.slc()
    slcReader.default = nisar.readers.slc()
    slcReader.doc = "the reader of NISAR compliant SLC products"


# end of file
