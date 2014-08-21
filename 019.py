#!/usr/bin/env python
"""Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

#-----------------
# Trivial solution
#-----------------
#
# For every year and every month we see if the first day is the one we are
# counting.
#
#
#def is_leap(year):
#    return (0 == year % 4) and ((0 == year % 100) == (0 == year % 400))
#
#def offset_month(month, year):
#    """
#    How many days the start of the week shifts for each month
#    """
#    if month == 2:
#        return 1 if is_leap(year) else 0
#    elif month in [4,6,9,11]:
#        return 2
#    else:
#        return 3
#
## We start on a Tuesday
#day = 1
#
## We are lookinf for a Sunday
#count_day = 6
#
#year = 1901
#end_year = 2000
#
#count = 0
#
## For each year
#while year <= end_year:
#    # For each month of the year
#    for month in xrange(1, 13):
#        # Increment counter if it starts with the day
#        if day == count_day:
#            count += 1
#
#        # Get the new start of the next month
#        day = (day + offset_month(month, year)) % 7
#    year += 1


#---------------
#Better solution
#---------------
#
# For this solution we'll work with a lookup table
# Since the number of days that fall on the first of each month is the same,
# but shifted.
#
# The table days_in_year is for years that start on Monday, if it starts on
# other day we just have to shift it.
#
# The days are different for leap years.

days_in_year = {
    False:[2,1,1,3,1,2,2],
    True :[3,1,1,2,2,1,2]
}

day = 1
count_day = 6
year = 1901
end_year = 2000
count = 0

# For each year
for y in xrange(year, end_year+1):
    # Since we know the range we are working with we don't bother to actually
    # look for the century exemption from leap year and we consider every year
    # divisible by 4 to be a leap year.
    leap = year & 3

    # We get the number of months that start with the day we are looking for.
    count += days_in_year[leap] [((7 - day) + count_day) % 7]

    # Calculate the start of next year
    day = (day + (366 if leap else 365)) % 7


print "\n", __doc__
print "There are {0} Sundays that fell on the first of the month in the twentieth century".format(count)
