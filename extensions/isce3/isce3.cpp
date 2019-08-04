// -*- C++ -*-

// for the build system
#include <portinfo>
// external dependencies
#include <Python.h>

// the module method declarations
#include "core/ellipsoid.h"


// put everything in my private namespace
namespace isce::extension {

    // the module method table
    PyMethodDef module_methods[] =
        {
         // ellipsoid
         // constructor
         {
          core::ellipsoid::ellipsoid__name__,
          core::ellipsoid::ellipsoid,
          METH_VARARGS,
          core::ellipsoid::ellipsoid__doc__
         },
         // access to the semi-major axis
         {
          core::ellipsoid::ellipsoid_semiMajor__name__,
          core::ellipsoid::ellipsoid_semiMajor,
          METH_VARARGS,
          core::ellipsoid::ellipsoid_semiMajor__doc__
         },
         // access to the semi-minor axis
         {
          core::ellipsoid::ellipsoid_semiMinor__name__,
          core::ellipsoid::ellipsoid_semiMinor,
          METH_VARARGS,
          core::ellipsoid::ellipsoid_semiMinor__doc__
         },
         // access to the eccentricity squared
         {
          core::ellipsoid::ellipsoid_eccentricitySquared__name__,
          core::ellipsoid::ellipsoid_eccentricitySquared,
          METH_VARARGS,
          core::ellipsoid::ellipsoid_eccentricitySquared__doc__
         },

         // sentinel
         {nullptr, nullptr, 0, nullptr}
        };

    // the module documentation string
    const char * const __doc__ = "isce3 extension module";

    // the module definition structure
    PyModuleDef module_definition =
        {
         // header
         PyModuleDef_HEAD_INIT,
         // the name of the module
         "isce3",
         // the module documentation string
         __doc__,
         // size of the per-interpreter state of the module; -1 if this state is global
         -1,
         // the methods defined in this module
         module_methods
        };
} // of namespace isce3


// initialization function for the module
// *must* be called PyInit_isce3
PyMODINIT_FUNC
PyInit_isce3()
{
    // create the module
    auto module = PyModule_Create(&isce::extension::module_definition);
    // if something went wrong
    if (!module) {
        // let python complain by raising an appropriate exception
        return nullptr;
    }

    // return the newly created module
    return module;
}


// end of file
