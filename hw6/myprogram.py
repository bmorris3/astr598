"""
ASTR 598 HW 6
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility

from mergesort import mergesort

# Twenty randomly shuffled integers from 1 to 21
integers = [16, 13, 10, 12, 15, 6, 11, 3, 19, 1, 20, 9, 7,
            2, 5, 4, 14, 18, 17, 8]

sorted_integers = mergesort(integers)

print(sorted_integers)