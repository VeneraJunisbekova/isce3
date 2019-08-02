// -*- C++ -*-
//
// eric m. gurrola
// california institute of technology, nasa
// (c) 2008-2019 all rights reserved
//

#pragma once

// ellipsoid extension private namespace
namespace isce {
  namespace extension {
    namespace core {

      // the constructor
      extern const char * const ellipsoid__name__;
      extern const char * const ellipsoid__doc__;
      PyObject * ellipsoid(PyObject *, PyObject *);

    }
  }
} // ellipsoid extension private namespace

// end-of-file

