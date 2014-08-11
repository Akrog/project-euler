#!/usr/bin/env python

"""Power digit sum
Problem 16
Published on 03 May 2002 at 06:00 pm [Server Time]
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

result = sum(map(int, str(1 << 1000)))

print "The sum of the digits of the number 2^1000 is", result
