#!/usr/bin/env python
"""Factorial digit sum

Problem 20
Published on 21 June 2002 at 06:00 pm [Server Time]
n! means n [x] (n [-] 1) [x] ... [x] 3 [x] 2 [x] 1

For example, 10! = 10 [x] 9 [x] ... [x] 3 [x] 2 [x] 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math

number = 100
result = sum(map(int, str(math.factorial(number))))

print "\n", __doc__
print "The sum of the digits of", number, "is", result
