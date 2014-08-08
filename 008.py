#!/usr/bin/env python
"""Largest product in a series
Problem 8
Published on 11 January 2002 at 06:00 pm [Server Time]
The four adjacent digits in the 1000-digit number that have the greatest product are 9 9 8 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the
value of this product?
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

import re
import itertools as it
import operator as op

# Get the data from the docstring and transform it into an array of ints
data = re.search("(\d{50}\n){20}", __doc__)
digitNumber = map(int, data.group().replace("\n",""))

numAdj = 13

print "\n", __doc__

#------------------
#One-liner solution
#------------------
#result = max ([(reduce(op.mul, it.islice(digitNumber,x,x+numAdj)), digitNumber[x:x+numAdj])
#               for x in xrange(len(digitNumber)-numAdj+1)])

#-------------------------------------------------------
#Same as before but easier to read and uses less memory
#-------------------------------------------------------
result = (0,None)
for x in xrange(len(digitNumber)-numAdj+1):
    s = it.islice(digitNumber, x, x+numAdj)
    m = reduce(op.mul, s)
    if m > result[0]:
        result=(m,digitNumber[x:x+numAdj])

print "The {} adjacent digits in the 1000-digit number that have the greatest product are\n\t{} = {}".format(numAdj, " * ".join(map(str,result[1])), result[0])
