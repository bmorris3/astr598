"""
ASTR 598 HW 6
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility
import numpy as np
import time
import matplotlib.pyplot as plt

from mergesort import mergesort

sizes = [1e2, 1e4, 1e6, 1e8]
runtimes = []
n_trials = 2
for size in sizes:
    int_list = np.random.randint(0, 1000, size)
    runtime = []
    for trial in range(n_trials):
        start = time.time()
        mergesort(int_list)
        end = time.time()
        runtime.append(end-start)
    print(runtime)
    runtimes.append(np.mean(runtime))

plt.loglog(sizes, runtimes)
plt.xlabel('Array length')
plt.ylabel('Runtime [s]')
plt.savefig('runtime.png', bbox_inches='tight')
plt.close()