#!/usr/bin/env python
"""10001st prime
Problem 7
Published on 28 December 2001 at 06:00 pm [Server Time]
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

from common.primes import getPrime
import itertools as it

numPrime = 10001

print "\n", __doc__

# Option with zip: Worst idea ever.
#result = zip(xrange(numPrime+1), getPrime())[-1][1]

# Option with a loop
#p = getPrime()
#for n in xrange(numPrime+1):
#    result = next(p)
#return (result)

# Option with itertools
result = next(it.islice(getPrime(), numPrime-1, numPrime))

print "\nThe {}st prime number is {}".format(numPrime,result)
