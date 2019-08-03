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

}

// end-of-file
