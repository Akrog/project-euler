#!/usr/bin/env python
"""Maximum path sum II
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

print "\n", __doc__

# Proposed solution is the same as for problem 018, calculate the max path value
# for each node of the tree based on it's parents max path values.
# Once we reach the leafs, we have all max path values calculated and we just
# have to get the node that has the highest value.


# Create a bidimensional list with the triangle data from the docstring
with open('067_triangle.txt') as triangle:
    lines = triangle.read().splitlines()
    data = [map(int,l.split()) for l in lines]

# Create a copy of the triangle where we'll store the best path values as we
# calculate them.

paths = data[:]

# For each element of the tree that has a parent
for row in xrange(1,len(data)):
    # Leftmost node has only 1 possible path
    paths[row][0] += paths[row-1][0]

    # For all nodes with 2 parents calculate the path using the maximum path of
    # its parents.
    for column in xrange(1,row):
        paths[row][column] += max(paths[row-1][column-1], paths[row-1][column])

    # Rightmost node hast only 1 possible path
    paths[row][-1] += paths[row-1][-1]

# The maximum path value of the leafs is the solution
best = max(paths[-1])

print "The maximum total from top to bottom of the triangle above is:", best
