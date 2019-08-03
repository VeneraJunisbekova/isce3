// -*- C++ -*-
//
// eric m. gurrola
// california institute of technology, nasa jet propulsion laboratory
// (c) 2008-2019 all rights reserved
//

#pragma once

namespace isce::extension::core {

    // ellipsoid
    namespace ellipsoid {
        const char * const capsule_t = "isce.core.ellipsoid";
        void free(PyObject *);
    }

    // orbit
    namespace orbit {
        const char * const capsule_t = "isce.core.orbit";
        void free(PyObject *);
    }

}

// end-of-file
