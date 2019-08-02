#-*- coding: utf-8 -*-


# support
import nisar


# declaration
class Config(nisar.shells.command, family="nisar.cli.config"):
    """
    Display configuration information about the {nisar} package
    """


    # version info
    @nisar.export(tip="the version information")
    def version(self, **kwds):
        """
        Print the version of the nisar package
        """
        # print the version number
        print(f"{nisar.meta.version}")
        # all done
        return 0


    # configuration
    @nisar.export(tip="the top level installation directory")
    def prefix(self, **kwds):
        """
        Print the top level installation directory
        """
        # print the version number
        print(f"{nisar.prefix}")
        # all done
        return 0


    @nisar.export(tip="the directory with the executable scripts")
    def path(self, **kwds):
        """
        Print the location of the executable scripts
        """
        # print the version number
        print(f"{nisar.prefix}/bin")
        # all done
        return 0


    @nisar.export(tip="the directory with the python packages")
    def pythonpath(self, **kwds):
        """
        Print the directory with the python packages
        """
        # print the version number
        print(f"{nisar.home.parent}")
        # all done
        return 0



# end of file
