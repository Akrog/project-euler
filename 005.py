#!/usr/bin/env python
"""Smallest multiple
Problem 5
Published on 30 November 2001 at 06:00 pm [Server Time]
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

#----------------
#Trivial solution
#----------------
#def smallest_v0_BruteForce(max):
#    s = range(1, max+1)
#    result = max
#    while any (result%x != 0 for x in s):
#        result += 1
#    return result

#-------------------
#Less brute solution
#-------------------
def smallest(max):
    # We only check the higher half of the numbers, because we know that they
    # will also be divisible by it's counterpart on the other half (if they
    # are divisible by 20 they are divisible by 10)
    s = range((max/2)+1, max+1)

    # We start with max and check using a step of max because we know it has to
    # be a multiple of it and no number in between can be a multiple.
    result = max
    result += result%max
    while any (result%x != 0 for x in s):
        result += max
    return result


max = 20

print "\n", __doc__
result = smallest(max)
print "\nThe smallest number that is evenly divisible by all of the numbers from 1 to {} is {}".format(max, result)
