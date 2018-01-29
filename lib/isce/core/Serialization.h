//-*- C++ -*-
//-*- coding: utf-8 -*-
//
// Author: Bryan V. Riel
// Copyright 2018
//

#include <iostream>
#include <memory>
#include <cereal/types/memory.hpp>
#include <cereal/types/vector.hpp>
#include <cereal/archives/xml.hpp>

#include <isce/core/Ellipsoid.h>

namespace isce { namespace core {

    // Main template call for archiving any isce::core object
    template <typename T>
    void load_archive(std::string metadata, char * objectTag, T * object) {
        std::stringstream metastream;
        metastream << metadata;
        cereal::XMLInputArchive archive(metastream);
        archive(cereal::make_nvp(objectTag, (*object)));
    }

    // Definition for Ellipsoid
    template<class Archive>
    void serialize(Archive & archive, Ellipsoid & ellps) {
        archive(cereal::make_nvp("a", ellps.a),
                cereal::make_nvp("e2", ellps.e2));
    }

}}

// end of file
