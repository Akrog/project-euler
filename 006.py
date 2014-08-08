#!/usr/bin/env python
"""Sum square difference
Problem 6
Published on 14 December 2001 at 06:00 pm [Server Time]
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

print "\n", __doc__

num = 100

#----------------
#Trivial solution: 2*O(N)
#----------------
#s1 = sum(xrange(num+1)) ** 2
#s2 = sum(x**2 for x in xrange(num+1))
#result = s1 - s2

#---------------
#Better solution: O(1)
#---------------
# We know that the addition of 1 to N-1 = (N-1)*N/2 therefore the square of the
# sum of 1 to N is ((N+1)*N/2)^2
# I'm sure there's a mathematical deduction for a more beautifil ecuation of the
# sum of the squares, but I just deduced this one from looking at the first 20
# results, so it's a little rudimentary.
# There's a correlation between the sum of the numbers and the sum of
# the square of those numbers: sum(sqr([1-N]) = sum([1-N]) * (1+(N-1)*0.66666)

def addupto(n):
    return ((n+1)*n)/2

def sumsqr(N):
    return int(addupto(N) * (1+(N-1)*2/3.0))

s1 = addupto(num) ** 2
s2 = sumsqr(num)
result = s1 - s2

print "The difference between the square of the sum of the first {} natural numbers and sum of the squares is {} ({} - {})".format(num,result,s1,s2)
