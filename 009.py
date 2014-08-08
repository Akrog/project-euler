#!/usr/bin/env python
"""Special Pythagorean triplet
Published on 25 January 2002 at 06:00 pm [Server Time]
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
   a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

print "\n", __doc__

abc = 1000

result = [(a,b,abc-a-b)
          for a in xrange(abc)
          for b in xrange(a, abc)
          if (a < b < (abc-a-b)) and (a**2 + b**2 == (abc-a-b)**2)]

print "The Pythagorean triplet for which a + b + c = {0} is a={1[0]} b={1[1]} c={1[2]} and the product is {2}".format(abc, result[0], reduce(int.__mul__,result[0]))
