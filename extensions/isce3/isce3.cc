// -*- C++ -*-

// for the build system
#include <portinfo>
// external dependencies
#include <Python.h>
#include <iostream>
// the module method declarations
#include "core/ellipsoid.h"


// put everything in my private namespace
namespace isce {

    namespace extension {

    // the module method table
    PyMethodDef module_methods[] = {
        // ellipsoid
        // constructor
        {core::ellipsoid__name__, core::ellipsoid, METH_VARARGS, core::ellipsoid__doc__},

        // sentinel
        {nullptr, nullptr, 0, nullptr}
    };

    // the module documentation string
    const char * const __doc__ = "isce3 extension module";

    // the module definition structure
    PyModuleDef module_definition = {
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
    } //of namespace extension
} // of namespace isce3

// initialization function for the module
// *must* be called PyInit_isce3
PyMODINIT_FUNC
PyInit_isce3()
{
    // create the module
    PyObject * module = PyModule_Create(&isce::extension::module_definition);
    // check whether module creation succeeded and raise an exception if not
    if (!module) {
        return nullptr;
    }

    // return the newly created module
    return module;
}

// end of file
