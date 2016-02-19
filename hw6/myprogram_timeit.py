"""
ASTR 598 HW 6
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility
import numpy as np
import time
import matplotlib.pyplot as plt

from mergesort import mergesort

# Twenty randomly shuffled integers from 1 to 21
integers = [16, 13, 10, 12, 15, 6, 11, 3, 19, 1, 20, 9, 7,
            2, 5, 4, 14, 18, 17, 8]

sorted_integers = mergesort(integers)


sizes = [1e2, 1e4, 1e6, 1e8]
runtimes = []
for size in sizes:
    int_list = np.random.randint(0, 1000, size)
    start = time.time()
    mergesort(int_list)
    end = time.time()
    runtimes.append(end-start)

plt.loglog(sizes, runtimes)
plt.xlabel('Array length')
plt.ylabel('Runtime [s]')
plt.savefig('runtime.png', bbox_inches='tight')
plt.close()