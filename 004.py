#!/usr/bin/env python
"""Largest palindrome product
Problem 4
Published on 16 November 2001 at 06:00 pm [Server Time]
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")


#----------------
#Trivial solution
#----------------
#def largestPalindrome(numDigits):
#    start = 10**(numDigits-1)
#    end = 10**numDigits
#    allPalindromes = [(x*y, x, y)
#                      for x in xrange(start, end)
#                      for y in xrange(x,end) if (str(x*y) == str(x*y)[::-1])]
#    if allPalindromes:
#        return max(allPalindromes)
#    else:
#        return None

#-----------------------
#More efficient solution: Especially if you try with 4 digits instead of 3
#-----------------------
# Since we know that the maximum product of 2 numbers in the range [N*10^2 to
# (N+1)*10^2-1] is always smaller than the minimum of [(N+1)*10^2 to
# (N+2)*10^2-1]
# (Example max([800-899]*[800-899]) < min([900-999]*[900-999]))
# And we know that there will always be palindromes in any 10th region of the
# total range the more digits we work with the more palindromes there will be)
# We will only work with the biggest possible numbers, those that begin with 9.
def largestPalindrome(numDigits):
    if 1 == numDigits: return 9
    start = 9 * (10**(numDigits-1))
    end = 10**numDigits
    allPalindromes = [(x*y, x, y)
                      for x in xrange(start, end)
                      for y in xrange(x,end) if (str(x*y) == str(x*y)[::-1])]
    if allPalindromes:
        return max(allPalindromes)
    else:
        return None


numDigits = 3

print "\n", __doc__
result, x, y = largestPalindrome(numDigits)
print "The largest palindrome made from the product of two {0}-digit numbers is {1} ({2} x {3})\n".format(numDigits,result,x,y)
