#!/usr/bin/env python
"""Summation of primes
Published on 08 February 2002 at 06:00 pm [Server Time]
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

from common.primes import getPrime
import itertools as it

print "\n", __doc__

ceiling = 2000000
result = sum(it.takewhile(lambda x: x < ceiling, getPrime()))

print "The sum of all the primes below {} is {}".format(ceiling, result)
