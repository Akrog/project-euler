#!/usr/bin/env python

"""Longest Collatz sequence
Problem 14
Published on 05 April 2002 at 06:00 pm [Server Time]
The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

        13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")


def Collatz(n):
    i = n
    yield i
    while i > 1:
        if i&1 == 0:
            i >>= 1
        else:
            i = 3*i + 1
        yield i

print __doc__

maxCol = 1000000


#-----------------
#Trivial solution: Very slow
#-----------------
# We only need to check numbers we haven't passed through in previous Collatz
# sequences.
# So we use a set to keep track of what numbers we have already checked.
#
#pending = set(xrange(2,maxCol))
#max = (0,0)
#while pending:
#    # Get one of the pending elements
#    i = pending.pop()
#
#    # Construct its Collatz list
#    c = list(Collatz(i))
#
#    # See if it's better than current best
#    if len(c) > max[0]:
#        max = (len(c), i)
#
#    # Remove all elements we've visited from the pending list
#    pending.difference_update(c)

#----------------
#Better solution: Executes in less than 1/4 of the time of the Trivial solution
#----------------
# We start from the higher numbers we have to check.
# We keep track of the lengths of every Collatz sequence.
# Wen we reach a Collatz sequence we've already examined we use its stored
# length to calculate the current squence length.

import itertools as it

nextCollatz = lambda n: n >> 1 if n&1 == 0 else 3*n + 1

lengths = {1:1}
max = (1, 1)

pending = maxCol-1

for i in xrange(maxCol-1, 1, -1):
    # If we already have that Collatz sequence's length
    if i in lengths:
        continue

    # Get it's Collatz sequence until we reach a sequence we've already done
    new_path = list(it.takewhile(lambda c: c not in lengths, Collatz(i)))

    # We get the Collatz number that made us stop
    stop = nextCollatz(new_path[-1])
    length = lengths[stop] + len(new_path)

    # We store the lengths of the partial sequences we've traversed, but only if
    # they are within those we are going to check. We don't include those that
    # go beyond maxCol. It is faster this way.
    new_lengths = {k:l
                   for (k,l) in it.izip(new_path, it.count(length,-1))
                   if k < maxCol}

    # Update the lengths' dictionary
    lengths.update(new_lengths)

    # If this is the new max we store it
    if length > max[0]:
        max = (length,i)

    # Check if we have already checked all Collatz sequences
    pending -= len(new_path)
    if pending == 0:
        break


print "The longest chain is produced by starting number {} and consists of {} elements".format(max[1], max[0])
