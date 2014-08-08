#!/usr/bin/env python
"""Multiples of 3 and 5
Problem 1
Published on 05 October 2001 at 06:00 pm [Server Time]
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")


print "\n",__doc__

ceiling = 1000


#----------------
#Trivial solution: O(n)
#----------------
#result = sum([x for x in xrange(ceiling) if (0 == x%3) or (0 == x%5)])


#---------------
#Better solution: O(1)
#---------------
# The idea of this approach is that the sum of the numbers below N multiple of M
# is: M+2M+3M+4M+...+(N/M-1)*M = M * (1+2+3+4+...+(N-1))
# And we know that the addition of 1 to N-1 = (N-1)*N/2
# So we have that the sum of the numbers is: M * (((N-1) * N) / 2)
# For the complete solution we only have to add the sum of multipliers of 3 to
# the sum of multipliers of 5 and take out those of 15 as they were added twice.

def addMults(number, ceiling):
    ceil = (ceiling-1)/number
    addUpTo = (ceil * (ceil+1)) / 2
    return number * addUpTo

result = addMults(3,ceiling) + addMults(5,ceiling) - addMults(15,ceiling)

print "The sum of all the multiples of 3 or 5 below {0} is {1}".format(ceiling,result)
