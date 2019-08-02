#-*- coding: utf-8 -*-


# access the pyre framework
import pyre
# and my package
import nisar


# build my CLI action dispatcher
class Plexus(pyre.plexus, family="nisar.components.plexus"):
    """
    The main CLI action dispatcher
    """


    # install my action protocol
    from .Action import Action as pyre_action


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
        context['nisar'] = nisar  # my package
        # and chain up
        return super().pyre_interactiveSessionContext(context=context)


   # virtual filesystem configuration
    def pyre_mountApplicationFolders(self, pfs, prefix):
        """
        Explore the installation folders and construct my private filesystem
        """
        # chain up
        pfs = super().pyre_mountApplicationFolders(pfs=pfs, prefix=prefix)
        # all done
        return pfs


 # end of file
