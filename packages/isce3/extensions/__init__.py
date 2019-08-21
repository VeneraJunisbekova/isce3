#-*- coding: utf-8 -*-


# attempt to
try:
    # pull the pure CPU implementation and publish it;
    from . import isceextension as libisce
# if this fails
except ImportError:
    # there isn't very much we can do; isce3 is not installed correctly
    import journal
    # build a description
    msg = "cannot locate the extension module; is isce3 installed correctly?"
    # so complain
    journal.error("isce3").log(msg)
    # and bail
    raise SystemExit(1)


# end of file
