#/usr/bin/env python

import time
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args,**kw)
        te = time.time()
        print "   Time to execute {} with params ({},{}) is {:.2f} secs.".format(method.__name__, args, kw, te-ts)
        return result
    return timed
