// -*- C++ -*-
//
//  eric m. gurrola
// california institute of technology, nasa
// (c) 2008-2019 all rights reserved
//

#include <portinfo>
#include <Python.h>

#include <isce/core/Ellipsoid.h>

#include "ellipsoid.h"
#include "../capsules.h"

// construction
const char * const
isce::extension::core::
ellipsoid__name__ = "ellipsoid";

const char * const
isce::extension::core::
ellipsoid__doc__ = "allocate an ellipsoid with a given a and e2";

PyObject *
isce::extension::core::
ellipsoid(PyObject *, PyObject * args) {
    // place holders for the python arguments
    double a, e2;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "dd:ellipsoid", &a, &e2);
    // if something went wrong
    if(!status) return 0;

    //create an Ellipsoid for given semimajor axis and eccentricity-squared
    isce::core::Ellipsoid * elp = new isce::core::Ellipsoid(a, e2); 

    // wrap it in a capsule and return it
    return PyCapsule_New(elp, ellipsoid_t, freeEllipsoid);
}

// destructors
void
isce::extension::core::
freeEllipsoid(PyObject * capsule) {
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, isce::extension::core::ellipsoid_t)) return;
    // get the ellipsoid
    isce::core::Ellipsoid * elp =
        static_cast<isce::core::Ellipsoid *>(PyCapsule_GetPointer(capsule, isce::extension::core::ellipsoid_t));
    // deallocate
    delete elp;
    // and return
    return;
}

// end-of-file
