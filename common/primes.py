#!/usr/bin/env python

import math
import itertools as it

def getPrime_v0():
    prims = set()
    n = 1
    while True:
        n += 1
        while any(n%x == 0 for x in prims):
            n += 1
        prims.add(n)
        yield n

def getPrime_v1():
    prims = []
    yield 2
    n = 1
    while True:
        n += 2
        while any(n%x == 0 for x in prims):
            n += 2
        prims.append(n)
        yield n

def getPrime_v2():
    prims = []
    yield 2
    n = 1
    while True:
        n += 2
        ceil = type(n)(math.sqrt(n) + 1)
        while any(n%p == 0 for p in it.takewhile(lambda x: x <= ceil, prims)):
            n += 2
        prims.append(n)
        yield n


class GetPrime_v1:
    prims = [2, 3]

    def __init__(self):
        pass

    def __iter__(self):
        self.i = 0
        return self

    def next(self):
        self.i += 1
        if self.i <= len(GetPrime_v1.prims):
            return GetPrime_v1.prims[self.i-1]

        n = GetPrime_v1.prims[-1] + 2
        ceil = type(n)(math.sqrt(n) + 1)

        while any(n % p == 0
                  for p in it.takewhile(lambda x: x <= ceil,
                                        GetPrime_v1.prims)):
            n += 2

        GetPrime_v1.prims.append(n)
        return n


getPrime = getPrime_v2
GetPrime = GetPrime_v1

if __name__ == "__main__":
    import timing

    @timing.timeit
    def ncalls(iter ,n):
        return list(it.islice(iter, n))

    numPrims = 20000
    ops = [getPrime_v0, getPrime_v1, getPrime_v2]
    results = [ncalls(f(), numPrims) for f in ops]

    if any(results[0] != x for  x in results[1:]):
        print "Error in one of the getPrime funcions: {}".format(results)
    else:
        print "All getPrime functions are working correctly"
#        print "Calculated prims are", results[0]
