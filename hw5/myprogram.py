"""
ASTR 598 HW 5
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility

from queue import PriorityQueue

q = PriorityQueue()

# Twenty randomly shuffled integers from 1 to 21
integers = [16, 13, 10, 12, 15, 6, 11, 3, 19, 1, 20, 9, 7,
            2, 5, 4, 14, 18, 17, 8]

# Insert random integers into binary min heap
for integer in integers:
    q.insert(integer)

# Remove minimum from heap until it's empty
for i in range(len(integers)):
    print(q.del_min())
