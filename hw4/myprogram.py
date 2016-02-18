"""
ASTR 598 HW 4
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility

from queue import Queue

q = Queue()

ten_integers = [20, 5, 3, 8, 5, 35, 20, 1, 4, 0]

# Put the integers into the queue:
for integer in ten_integers:
    q.put(integer)

# Get the integers out of the queue:
for i in range(len(ten_integers)):
    print(q.get())
