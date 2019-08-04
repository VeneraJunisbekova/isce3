// -*- C++ -*-
//
// eric m. gurrola
// california institute of technology, nasa
// (c) 2008-2019 all rights reserved
//

#pragma once

// place everything in my namespace
namespace isce::extension::core::ellipsoid {

    // the constructor
    extern const char * const ellipsoid__name__;
    extern const char * const ellipsoid__doc__;
    PyObject * ellipsoid(PyObject *, PyObject *);

    // access to the semi-major axis
    extern const char * const ellipsoid_semiMajor__name__;
    extern const char * const ellipsoid_semiMajor__doc__;
    PyObject * ellipsoid_semiMajor(PyObject *, PyObject *);

    // access to the semi-minor axis
    extern const char * const ellipsoid_semiMinor__name__;
    extern const char * const ellipsoid_semiMinor__doc__;
    PyObject * ellipsoid_semiMinor(PyObject *, PyObject *);

    // access to the eccentricity squared
    extern const char * const ellipsoid_eccentricitySquared__name__;
    extern const char * const ellipsoid_eccentricitySquared__doc__;
    PyObject * ellipsoid_eccentricitySquared(PyObject *, PyObject *);

}

// end-of-file
