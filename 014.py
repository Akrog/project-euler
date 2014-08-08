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

# We only need to check numbers we haven't passed through in previous Collatz
# sequences.
# So we use a set to keep track of what numbers we have already checked.

pending = set(xrange(2,maxCol))

max = (0,0)
while pending:
    # Get one of the pending elements
    i = pending.pop()

    # Construct its Collatz list
    c = list(Collatz(i))

    # See if it's better than current best
    if len(c) > max[0]:
        max = (len(c), i)

    # Remove all elements we've visited from the pending list
    pending.difference_update(c)

print "The longest chain is produced by starting number {} and consists of {} elements".format(max[1], max[0])
