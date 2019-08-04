# -*- Makefile -*-

# project meta-data
isce.major := 3
isce.minor := 0

# isce consists of python packages
isce.packages := isce.pkg
# libraries
isce.libraries := isce.lib cereal.lib
# python extensions
isce.extensions := isce.ext
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

# the isce extension
isce.ext.pkg := isce.pkg
isce.ext.wraps := isce.lib
isce.ext.root := extensions/isce3/
isce.ext.stem := isce3
isce.ext.extern := isce.lib gdal hdf5 mpi numpy pyre python

# the cereal lib meta-data
cereal.lib.root := contrib/cereal/include/cereal/
cereal.lib.stem := cereal

# external package configuration
fftw.flavor := 3 3_threads 3f 3f_threads

# end of file
