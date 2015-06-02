import logging
import time

from functools import wraps


logger = logging.getLogger('timing')


def timeit(_fn=None, exc_info=False):
    """timing decorator via:
    http://www.zopyx.de/blog/a-python-decorator-for-measuring-the-execution-time-of-methods

    @timeit
    def mymethod(arg, arg2):
        return arg + arg2

    -- OR --

    @timeit(exc_info=False) # to hide execution data
    def mymeth(arg1, arg2):
        return arg1 + arg2

    """
    def _timeit(method):
        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()

            if exc_info:
                logger.info('%s.%s %2.3fs (%r, %r)',
                            method.__module__, method.__name__, te - ts, args, kw)
            else:
                logger.info('%s.%s %2.3fs',
                            method.__module__, method.__name__, te - ts)
            return result
        timed.__name__ = method.__name__
        return wraps(method)(timed)
    if callable(_fn):
        return _timeit(_fn)
    else:
        return _timeit
