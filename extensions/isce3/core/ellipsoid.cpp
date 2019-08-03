// -*- C++ -*-
//
//  eric m. gurrola
// california institute of technology, nasa
// (c) 2008-2019 all rights reserved
//

// for the build system
#include <portinfo>
// externals
#include <Python.h>
// the isce objects
#include <isce/core/Ellipsoid.h>

// my methods
#include "../capsules.h"
#include "ellipsoid.h"


// local type aliases
namespace isce::extension::core::ellipsoid {
    // local type aliases
    using ellipsoid_t = isce::core::Ellipsoid;
}


// construction
const char * const
isce::extension::core::ellipsoid::
ellipsoid__name__ = "ellipsoid";

const char * const
isce::extension::core::ellipsoid::
ellipsoid__doc__ = "make a new ellipsoid";

PyObject *
isce::extension::core::ellipsoid::
ellipsoid(PyObject *, PyObject * args) {
    // place holders for the python arguments
    double a, e2;
    // unpack the argument tuple
    auto status = PyArg_ParseTuple(args, "dd:ellipsoid", &a, &e2);
    // if something went wrong
    if (!status) {
        // let python raise an appropriate exception
        return nullptr;
    }

    // create an ellipsoid with the given parameters
    auto elp = new ellipsoid_t(a, e2);

    // wrap it in a capsule and return it
    return PyCapsule_New(elp, capsule_t, free);
}


// helpers
// destructors
void
isce::extension::core::ellipsoid::
free(PyObject * capsule) {
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, capsule_t)) return;
    // get the ellipsoid pointer
    auto elp = static_cast<ellipsoid_t *>(PyCapsule_GetPointer(capsule, capsule_t));
    // deallocate it
    delete elp;
    // and return
    return;
}

// end-of-file
