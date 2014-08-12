#!/usr/bin/env python
"""Number letter counts
Problem 17
Published on 17 May 2002 at 06:00 pm [Server Time]
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

print "\n", __doc__

#--------
#Option 1: Brute force
#--------
# We could create a function to generate de words (numb2word) or use an already
# existing library like pynum2word and then do:
#
#import itertools as it
#result = reduce(lambda total, word: total + len(word.translate(None," -")),
#                it.imap(num2word, xrange(1, max_number+1)),
#                0)

#--------
#Option 2: Smart way
#--------
# We don't actually need to generate the words, we know the amount of times each
# word is going to happen.
# For example, we know that the word "hundred" will appear exactly 900 times
# between 1 and 1000.

units = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
         8:"eight", 9:"nine"}
teens = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
         15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
         19:"nineteen"}
tenths = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
          70:"seventy", 80:"eighty", 90:"ninety"}

sum_map = lambda dic: sum(map(len, dic.values()))

s1_9      = sum_map(units)
below100  = 9 * s1_9 + sum_map(teens) + 10 * sum_map(tenths)
below1000 = 100 * s1_9 + 900 * len("hundred") + 891 * len("and") + 10 * below100
upto1000  = below1000 + len(units[1]) + len("thousand")

print "The numbers of letter used for writting all the numbers from 1 to 1000 inclusive are", upto1000
