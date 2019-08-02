#-*- coding: utf-8 -*-


# support
import isce3


# declaration
class About(isce3.shells.command, family="isce3.cli.about"):
    """
    Display information about the app
    """


    # administrative
    @isce3.export
    def copyright(self, plexus, **kwds):
        """
        Print the copyright note of the isce3 package
        """
        # grab a channel
        channel = plexus.info
        # log the copyright note
        channel.log(isce3.meta.copyright)
        # all done
        return


    @isce3.export
    def credits(self, plexus, **kwds):
        """
        Print the isce3 package acknowledgments
        """
        # grab a channel
        channel = plexus.info
        # log the copyright note
        channel.log(isce3.meta.acknowledgments)
        # all done
        return


    @isce3.export
    def license(self, plexus, **kwds):
        """
        Print the isce3 package license
        """
        # grab a channel
        channel = plexus.info
        # log the copyright note
        channel.log(isce3.meta.license)
        # all done
        return


# end of file
