#-*- coding: utf-8 -*-


# support
import nisar


# declaration
class About(nisar.shells.command, family="nisar.cli.about"):
    """
    Display human readable information about the app
    """


    # administrative
    @nisar.export(tip="the copyright note")
    def copyright(self, plexus, **kwds):
        """
        Print the copyright note of the nisar package
        """
        # grab a channel
        channel = plexus.info
        # log the copyright note
        channel.log(nisar.meta.copyright)
        # all done
        return


    @nisar.export(tip="acknowledgments and sponsor info")
    def credits(self, plexus, **kwds):
        """
        Print the nisar package acknowledgments
        """
        # grab a channel
        channel = plexus.info
        # log the copyright note
        channel.log(nisar.meta.acknowledgments)
        # all done
        return


    @nisar.export(tip="licensing information")
    def license(self, plexus, **kwds):
        """
        Print the nisar package license
        """
        # grab a channel
        channel = plexus.info
        # log the copyright note
        channel.log(nisar.meta.license)
        # all done
        return


# end of file
