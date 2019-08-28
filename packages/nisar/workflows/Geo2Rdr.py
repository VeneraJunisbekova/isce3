#-*- coding: utf-8 -*-

# support
import isce3
import nisar


# the {geo2rdr} workflow with {nisar} specific defaults
class Geo2Rdr(isce3.workflows.geo2rdr(), family="nisar.workflows.geo2rdr"):
    """
    Compute the transformation from geodetic to radar coordinates for a given NISAR compliant
    SLC product
    """


    # override the SLC reader to install the {nisar} specific defaults
    slcReader = nisar.protocols.readers.slc()
    slcReader.default = nisar.readers.slc()
    slcReader.doc = "the reader of NISAR compliant SLC products"


# end of file
