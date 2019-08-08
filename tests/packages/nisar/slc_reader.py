#!/usr/bin/env python3

import os
from nisar.products.readers import SLC

def main():
    curpath = os.path.dirname(os.path.realpath(__file__))
    print('dir_path = {}'.format(curpath))
    h5file = os.path.join(curpath, '../../../../', 'isce3_test_data/llh_uavsar_rosamond.h5')
    slc = SLC(hdf5file=h5file)
    slc._parse(h5file)
    print("slc.filename             = {}".format(slc.filename))
    print("slc.getZeroDopplerTime() = {}".format(slc.getZeroDopplerTime()))
    print("slc.getSlantRange() = {}".format(slc.getSlantRange()))
    print("slc.frequencies          = {}".format(slc.frequencies))
    print("slc.polarizations        = {}".format(slc.polarizations))
#    print("slc.getOrbit() = {}".format(slc.getOrbit()))
#    print("slc.computeBoundingBox() = {}".format(slc.computeBoundingBox()))
#    print("doppler centroid       = {}".format(slc.getDopplerCentroid()))

    """
    ['CFPath', 'CategoryMismatchError', 'ConfigurationError', 'ConstraintViolationError', 'FrameworkError', 'GridPath', 'IdentificationPath', 'MetadataPath', 'PrivateInventory', 'ProcessingInformationPath', 'ProductPath', 'ProtocolCompatibilityError', 'PublicInventory', 'PyreError', 'ResolutionError', 'RootPath', 'SwathPath', 'TraitNotFoundError', '_CFPath', '_GridPath', '_IdentificationPath', '_MetadataPath', '_ProcessingInformation', '_ProductType', '_RootPath', '_SwathPath', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parse', 'computeBoundingBox', 'dashboard', 'filename', 'frequencies', 'getDopplerCentroid', 'getGridMetadata', 'getOrbit', 'getRadarGrid', 'getSlantRange', 'getSwathMetadata', 'getZeroDopplerTime', 'identification', 'parsePolarizations', 'polarizations', 'populateIdentification', 'productType', 'productValidationType', 'pyre_application', 'pyre_behaviors', 'pyre_classConfigured', 'pyre_classInitialized', 'pyre_classRegistered', 'pyre_classWhere', 'pyre_configurables', 'pyre_configurationErrors', 'pyre_configurator', 'pyre_configured', 'pyre_executive', 'pyre_facilities', 'pyre_family', 'pyre_familyFragments', 'pyre_fileserver', 'pyre_finalized', 'pyre_getExtent', 'pyre_getTrait', 'pyre_help', 'pyre_host', 'pyre_how', 'pyre_implements', 'pyre_inheritedTraits', 'pyre_initializationErrors', 'pyre_initialized', 'pyre_internal', 'pyre_inventory', 'pyre_isCompatible', 'pyre_isComponent', 'pyre_isProtocol', 'pyre_isPublicClass', 'pyre_key', 'pyre_localBehaviors', 'pyre_localConfigurables', 'pyre_localFacilities', 'pyre_localProperties', 'pyre_localTraits', 'pyre_locator', 'pyre_name', 'pyre_namemap', 'pyre_nameserver', 'pyre_normalizeInstanceName', 'pyre_package', 'pyre_pedigree', 'pyre_properties', 'pyre_public', 'pyre_registered', 'pyre_registrar', 'pyre_renderConfiguration', 'pyre_schema', 'pyre_setTrait', 'pyre_showBehaviors', 'pyre_showConfigurables', 'pyre_showConfiguration', 'pyre_showSummary', 'pyre_slot', 'pyre_spec', 'pyre_trait', 'pyre_traitmap', 'pyre_traits', 'pyre_user', 'pyre_where', 'validate']
    """

if __name__ == "__main__":
    status = main()
    raise SystemExit(status)
