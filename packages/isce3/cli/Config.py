#-*- coding: utf-8 -*-


# support
import isce3


# declaration
class Config(isce3.shells.command, family="isce3.cli.config"):
    """
    Display configuration information about the {isce3} package
    """


    # version info
    @isce3.export(tip="the version information")
    def version(self, **kwds):
        """
        Print the version of the isce3 package
        """
        # print the version number
        print(f"{isce3.meta.version}")
        # all done
        return 0


    # configuration
    @isce3.export(tip="the top level installation directory")
    def prefix(self, **kwds):
        """
        Print the top level installation directory
        """
        # print the version number
        print(f"{isce3.prefix}")
        # all done
        return 0


    @isce3.export(tip="the directory with the executable scripts")
    def path(self, **kwds):
        """
        Print the location of the executable scripts
        """
        # print the version number
        print(f"{isce3.prefix}/bin")
        # all done
        return 0


    @isce3.export(tip="the directory with the python packages")
    def pythonpath(self, **kwds):
        """
        Print the directory with the python packages
        """
        # print the version number
        print(f"{isce3.home.parent}")
        # all done
        return 0


    @isce3.export(tip="the location of the {isce3} headers")
    def incpath(self, **kwds):
        """
        Print the locations of the {isce3} headers
        """
        # print the version number
        print(f"{isce3.prefix}/include")
        # all done
        return 0


    @isce3.export(tip="the location of the {isce3} libraries")
    def libpath(self, **kwds):
        """
        Print the locations of the {isce3} libraries
        """
        # print the version number
        print(f"{isce3.prefix}/lib")
        # all done
        return 0


# end of file
