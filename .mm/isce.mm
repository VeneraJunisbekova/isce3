# -*- Makefile -*-

# project meta-data
isce.major := 3
isce.minor := 0

# isce consists of python packages
isce.packages := isce.pkg
# libraries
isce.libraries := isce.lib cereal.lib
# python extensions
isce.extensions := isce.capi isce.cython
# and test suites
isce.tests :=

# the isce python package
isce.pkg.stem := isce3
isce.pkg.root := packages/isce3/
isce.pkg.ext := extensions/
isce.pkg.drivers := isce3

# the isce lib meta-data
isce.lib.root := lib/isce/
isce.lib.stem := isce
isce.lib.libstem := isce-$(isce.major).$(isce.minor)
isce.lib.extern := gdal hdf5 mpi fftw pyre
isce.lib.prerequisites := cereal.lib
isce.lib.c++.flags += $($(compiler.c++).std.c++17)

# the isce extension that's built with the C API
isce.capi.pkg := isce.pkg
isce.capi.wraps := isce.lib
isce.capi.root := extensions/isce3/
isce.capi.stem := isce3
isce.capi.extern := isce.lib gdal hdf5 mpi numpy pyre python

# the isce extension that's built with cython
isce.cython.pkg := isce.pkg
isce.cython.wraps := isce.lib
isce.cython.root := extensions/cython/isce/
isce.cython.stem := isceextension
isce.cython.capsule :=
isce.cython.extern := isce.lib gdal hdf5 mpi numpy pyre python

# the cereal lib meta-data
cereal.lib.root := contrib/cereal/include/cereal/
cereal.lib.stem := cereal

# external package configuration
fftw.flavor := 3 3_threads 3f 3f_threads

# end of file
