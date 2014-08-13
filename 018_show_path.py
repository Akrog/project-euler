#!/usr/bin/env python
"""Maximum path sum I

Problem 18
Published on 31 May 2002 at 06:00 pm [Server Time]
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below [and print the path]:

                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, {Problem 67}, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

import re
import itertools


# Proposed solution is to calculate the max path value for each node of the tree
# based on it's parents max path values.
# Once we reach the leafs, we have all max path values calculated and we just
# have to get the node that has the highest value.
#
# In this version of the solution we are assuming that we receive a tree as
# the data structure we have to solve the problem instead of the raw data.
#
# We also assume we want to know what values we visited to achieve the result.


# Sinmple Tree class structure.
class Tree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None   # Parent for the max path
        self.total = 0       # Total max path value coming from parent


# This is the function that resolves the problem given the root of a tree
def getMaxRoute(tree):
    # Set path info for root
    tree.total = tree.value
    tree.parent = None

    # For now we create a false maxNode
    maxNode = tree

    # We are going to traverse the tree going to the left and for each node we'll
    # traverse all its right children.
    # The idea is that we'll assign ourselves to the left children as the best
    # possible path and we'll only check with the right child to see if we are
    # a better alternative to the path it has already stored.

    nodeleft = tree
    while nodeleft.left:
        me = nodeleft
        while me.right:
            # The left child has never been visited, so for the time being we
            # are the best path to that child
            me.left.total = me.total + me.left.value
            me.left.parent = me

            # The right child may have been visited, we have to check if we are
            # a better alternative.
            if me.right.total < me.total + me.right.value:
                me.right.total = me.total + me.right.value
                me.right.parent = me

            me = me.right

        # If we are in a leaf we have to check if we are a new max.
        else:
            if me.total > maxNode.total:
                maxNode = me
        nodeleft = nodeleft.left

    # If we are in the leftmost child we must check if this is the new max.
    else:
        if me.total > maxNode.total:
            maxNode = me

    # Now we reconstruct the max path by reversing the parents path
    node, maxPath = maxNode, []
    while node:
        maxPath.insert(0, node.value)
        node = node.parent

    return (maxNode.total, maxPath)


# Prepare the tree
def prepareTree(data):
    # Create a bidimensional list with the triangle data from the docstring
    r = re.search("\n(?P<data>\s+?(\d\d(\s+|\n))+)", data)
    lines = r.group('data')[1:-2].split('\n')
    data = [map(int,l.split()) for l in lines]

    # Transform the bidimensional list of integers to tree nodes
    tree = [map(Tree, row) for row in data]

    # Set the root
    root = tree[0][0]

    # For every parent we asign the kids
    for row in xrange(len(tree)-1):
        for column in xrange(len(data[row])):
            tree[row][column].left = tree[row+1][column]
            tree[row][column].right = tree[row+1][column+1]

    return root


if __name__ == "__main__":
    # Get the tree
    tree = prepareTree(__doc__)

    # Find the max route
    result = getMaxRoute(tree)

    print "\n", __doc__
    print "The maximum total from top to bottom of the triangle above is", \
          result[0], "using path", result[1]
