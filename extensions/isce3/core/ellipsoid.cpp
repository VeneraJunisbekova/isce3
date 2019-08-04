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


// access to the semi-major axis
const char * const
isce::extension::core::ellipsoid::
ellipsoid_semiMajor__name__ = "ellipsoid_semiMajor";

const char * const
isce::extension::core::ellipsoid::
ellipsoid_semiMajor__doc__ = "retrieve the value of the semi-major axis";

PyObject *
isce::extension::core::ellipsoid::
ellipsoid_semiMajor(PyObject *, PyObject * args) {
    // the capsule
    PyObject * capsule;
    // unpack the argument tuple
    auto status = PyArg_ParseTuple(args,
                                   "O!:ellipsoid_semiMajor",
                                   &PyCapsule_Type, &capsule);
    // if something went wrong
    if (!status) {
        // let python raise an appropriate exception
        return nullptr;
    }
    // if we git the wrong capsule
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        // set the exception type
        PyErr_SetString(PyExc_TypeError, "invalid ellipsoid capsule");
        // and raise an exception
        return nullptr;
    }

    // get the ellipsoid
    auto elp = static_cast<const ellipsoid_t *>(PyCapsule_GetPointer(capsule, capsule_t));
    // ask it for its semi-major axis
    auto a = elp->a();

    // convert it to a python double and return it
    return PyFloat_FromDouble(a);
}


// access to the semi-minor axis
const char * const
isce::extension::core::ellipsoid::
ellipsoid_semiMinor__name__ = "ellipsoid_semiMinor";

const char * const
isce::extension::core::ellipsoid::
ellipsoid_semiMinor__doc__ = "retrieve the value of the semi-minor axis";

PyObject *
isce::extension::core::ellipsoid::
ellipsoid_semiMinor(PyObject *, PyObject * args) {
    // the capsule
    PyObject * capsule;
    // unpack the argument tuple
    auto status = PyArg_ParseTuple(args,
                                   "O!:ellipsoid_semiMinor",
                                   &PyCapsule_Type, &capsule);
    // if something went wrong
    if (!status) {
        // let python raise an appropriate exception
        return nullptr;
    }
    // if we git the wrong capsule
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        // set the exception type
        PyErr_SetString(PyExc_TypeError, "invalid ellipsoid capsule");
        // and raise an exception
        return nullptr;
    }

    // get the ellipsoid
    auto elp = static_cast<const ellipsoid_t *>(PyCapsule_GetPointer(capsule, capsule_t));
    // ask it for its semi-minor axis
    auto b = elp->b();

    // convert it to a python double and return it
    return PyFloat_FromDouble(b);
}


// access to the eccentricity squared
const char * const
isce::extension::core::ellipsoid::
ellipsoid_eccentricitySquared__name__ = "ellipsoid_eccentricitySquared";

const char * const
isce::extension::core::ellipsoid::
ellipsoid_eccentricitySquared__doc__ = "retrieve the value of the eccentricity squared";

PyObject *
isce::extension::core::ellipsoid::
ellipsoid_eccentricitySquared(PyObject *, PyObject * args) {
    // the capsule
    PyObject * capsule;
    // unpack the argument tuple
    auto status = PyArg_ParseTuple(args,
                                   "O!:ellipsoid_eccentricitySquared",
                                   &PyCapsule_Type, &capsule);
    // if something went wrong
    if (!status) {
        // let python raise an appropriate exception
        return nullptr;
    }
    // if we git the wrong capsule
    if (!PyCapsule_IsValid(capsule, capsule_t)) {
        // set the exception type
        PyErr_SetString(PyExc_TypeError, "invalid ellipsoid capsule");
        // and raise an exception
        return nullptr;
    }

    // get the ellipsoid
    auto elp = static_cast<const ellipsoid_t *>(PyCapsule_GetPointer(capsule, capsule_t));
    // ask it for its eccentricity squared
    auto e2 = elp->e2();

    // convert it to a python double and return it
    return PyFloat_FromDouble(e2);
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
