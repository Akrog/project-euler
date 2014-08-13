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

Find the maximum total from top to bottom of the triangle below:

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

print "\n", __doc__

# Proposed solution is to calculate the max path value for each node of the tree
# based on it's parents max path values.
# Once we reach the leafs, we have all max path values calculated and we just
# have to get the node that has the highest value.


# Create a bidimensional list with the triangle data from the docstring
r = re.search("\n(?P<data>\s+?(\d\d(\s+|\n))+)",__doc__)
lines = r.group('data')[1:-2].split('\n')
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
