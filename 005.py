#!/usr/bin/env python
"""Smallest multiple
Problem 5
Published on 30 November 2001 at 06:00 pm [Server Time]
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")

#----------------
#Trivial solution
#----------------
#def smallest_v0_BruteForce(max):
#    s = range(1, max+1)
#    result = max
#    while any (result%x != 0 for x in s):
#        result += 1
#    return result

#-------------------
#Less brute solution
#-------------------
#def smallest(max):
#    # We only check the higher half of the numbers, because we know that they
#    # will also be divisible by it's counterpart on the other half (if they
#    # are divisible by 20 they are divisible by 10)
#    s = range((max/2)+1, max+1)
#
#    # We start with max and check using a step of max because we know it has to
#    # be a multiple of it and no number in between can be a multiple.
#    result = max
#    result += result%max
#    while any (result%x != 0 for x in s):
#        result += max
#    return result

#-------------------
# Best solution: LCM
#-------------------
#
# If we stop thinking about the problem as a programming problem we'll realize
# this is actually a high-school math problem.
#
# You just need to find out the Least Common Multiple of those numbers.
#
# We can remove half of them since they are factors of the other half.
#

def lcm(numbers):
    """
    Calculate the Least Common Multiple of an iterable
    There are several ways to get the LCM:
       - Reduction by the GCD
       - Prime factorization
       - Using a table
    This implementation uses the last approach, using a table. If there where
    only 2 numbers I would have probably used the reduction by the GCD method.
    """
    import operator
    from common.primes import getPrime

    if not hasattr(numbers, '__iter__'):
        if isinstance(numbers, (int, long)):
            return numbers
        else:
            raise Exception("That's not a number")

    # Create table with all numbers that are not 1
    result=[]
    table = [n for n in numbers if n > 1]

    # To reduce the table we'll only use prime numbers
    primes = iter(getPrime())
    get_next_prime = True

    # Since we'll be removing all numbers that reach 1
    # We'll continue until we empty the table
    while table:
        # If the last iteration didn't get any reduction
        if get_next_prime:
            prime = next(primes)

        # By default we assume we won't get any reduction
        get_next_prime = True

        # We go trhough the table in reverse order so we can remove rows
        for i in xrange(len(table)-1, -1, -1):
            # If current prime number is a factor
            if table[i] % prime == 0:
                # If this is the first number in this iteration that is a factor
                # we add the prime number to the solution
                if get_next_prime:
                    get_next_prime = False
                    result.append(prime)

                # Reduce the number and remove if necessary
                table[i] /= prime
                if (table[i] == 1):
                    del table[i]

    # The solution is the result of multiplying all prime factors.
    return reduce(operator.mul, result)

max = 20

print "\n", __doc__
result = lcm(range((max/2)+1 ,max+1))
print "\nThe smallest number that is evenly divisible by all of the numbers from 1 to {} is {}".format(max, result)
