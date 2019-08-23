#-*- coding: utf-8 -*-


# support
import isce3
# and my package
import nisar


# build my CLI action dispatcher by extending the one from {isce3}
class Plexus(isce3.shells.plexus, family="nisar.components.plexus"):
    """
    The main CLI action dispatcher
    """


    # pyre framework hooks
    def pyre_banner(self):
        """
        Generate the help banner
        """
        # show the license header
        return nisar.meta.header


    # interactive session management
    def pyre_interactiveSessionContext(self, context=None):
        """
        Go interactive
        """
        # prime the execution context
        context = context or {}
        # grant access to my package
        context['nisar'] = nisar
        # and chain up
        return super().pyre_interactiveSessionContext(context=context)


 # end of file
