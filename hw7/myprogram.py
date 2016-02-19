"""
ASTR 598 HW 7
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility

from bst import BinarySearchTree

# Generate some random integers:
import numpy as np
integers = np.random.randint(0, 1000, size=100).tolist()

bst = BinarySearchTree()

# Insert some random integers into the binary search tree:
for integer in integers:
    bst.insert(integer)

# Traverse that tree in order (notice they're in order, wahoo!)
print("Traverse:")
bst.traverse()

# Find min, max:
print("Min: {0}, max: {1}".format(bst.min(), bst.max()))
