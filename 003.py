#!/usr/bin/env python
"""Largest prime factor
Problem 3
Published on 02 November 2001 at 06:00 pm [Server Time]
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

import common.primes as primes

def getMaxPrimeFactor(number):
    # If we assume we always have a solution we can remove the ceiling check.
    ceiling = number / 2
    p = primes.getPrime()
    solution = 1
    while number != 1:
        n = next(p)
        while number%n != 0:
            n = next(p)
            # If there's no perfect solution, we got as close as we could
            if n > ceiling:
                return solution
        solution = n
        number /= n
    return solution

number = 600851475143

print "\n", __doc__
result = getMaxPrimeFactor(number)
print "Largest prime factor of number {0} is {1}".format(number,result)
