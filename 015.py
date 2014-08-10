#!/usr/bin/env python

"""Lattice paths
Problem 15
Published on 19 April 2002 at 06:00 pm [Server Time]
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

__   _    _
  |   |_   |
  |     |  |_

|__  |_   |
   |   |_ |__

How many such routes are there through a 20x20 grid?
"""

import sys
if (2,7) > sys.version_info or (3,0) <= sys.version_info:
    import warnings
    warnings.warn("Code intended for Python 2.7.x")


import itertools as it


#----------------
#Trivial Solution: Doesn't finish
#----------------
# If we needed to know all possible paths, then we could build them with the following code,
# but since there are several billion different paths and we don't need to build them, we just
# need to know the number of different paths, we do it another way.
#
#movs=["down","right"]
#result = [[]]
#grid_size=6
#for x in xrange(2*grid_size):
#    r = result
#    result = []
#    for e in r:
#        for m in movs:
#            if e.count(m) < grid_size:
#                result.append(e + [m])


#---------------
#Better solution
#---------------
# The way I'm finding out the number of paths is by calculating the number of
# paths in each intersection of lines and knowing that each intersection has as
# many paths as his 2 connections added together.
#
#  20 __10 __ 4 __ 1
#   |    |    |    |
#   |    |    |    |
#  10 -- 6 -- 3 -- 1
#   |    |    |    |
#   |    |    |    |
#   4 -- 3 -- 2 -- 1
#   |    |    |    |
#   |    |    |    |
#   1 -- 1 -- 1 -- 0
#
# If you have a closer look you'll realize that it's simmetrical along the
# diagonal. So we don't have to actually build the whole tree, just half of it
# will be enough.
#
#class Tree():
#    def __init__(self, value, right=None, left=None):
#        self.value = value
#        self.right = right
#        self.left = left
#
#    def leftmost(self):
#        t = self
#        while t.left:
#            t = t.left
#        return t
#
#def latticePath():
#    t = Tree(2)
#    level = 0
#    yield 2
#
#    while True:
#        n = t.leftmost()
#        n.left = Tree(n.value+1)
#        for i in xrange(level):
#            n.left.right = Tree(n.left.value + n.right.value)
#            n.right.left = n.left.right
#            n = n.right
#        newVal = n.left.value * 2
#        n.left.right = Tree(newVal)
#        level += 1
#        yield newVal
#grid_size = 20
#lattice_paths = list(it.islice(latticePath(), grid_size-1, grid_size))[0]
#print lattice_paths

#-------------
#Best solution
#-------------
#We can do the same thing in-place, without building a tree, just using a list
def calclattice(gsize):
    solutions = range(2,2+gsize)
    for i in xrange(1,len(solutions)):
        solutions[i] *= 2
        for j in xrange(i+1, len(solutions)):
            solutions[j] += solutions[j-1]
    return solutions[-1]

print "\n", __doc__

grid_size = 20
lattice_paths = calclattice(grid_size)

print "In a {0} x {0} grid there are {1} Lattice Paths".format(grid_size, lattice_paths)
