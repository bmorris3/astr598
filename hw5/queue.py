"""
ASTR 598 HW 5
Brett Morris
"""


class PriorityQueue(object):
    def __init__(self, max=100):
        """
        Construct a PriorityQueue object
        """
        self.a = [0]
        self.N = 0
        self.max = max

    def insert(self, i):
        if self.N + i > self.max:
            raise ValueError("Cannot insert above max={0}".format(self.max))

        self.a.append(i)
        self.N += 1
        k = self.N

        while k > 1 and self.a[k//2] > self.a[k]:
            self.a[k//2], self.a[k] = self.a[k], self.a[k//2]
            k //= 2

    def del_min(self):
        old_min = self.min()

        # Reset root with last value
        self.a[1] = self.a[self.N]
        # Reset last child with zero
        self.a[self.N] = 0
        self.N -= 1

        k = 1
        while 2*k <= self.N:

            # If we reached end of the branch and it's the only child, or
            # the left child is smaller than right child
            if 2*k == self.N or self.a[2*k] < self.a[2*k+1]:
                j = 2*k  # smaller/only child
            # Otherwise if right child is smaller
            else:
                j = 2*k+1 # smaller child

            if self.a[k] > self.a[j]:
                self.a[k], self.a[j] = self.a[j], self.a[k]
                k = j
            else:
                # All conditions are satisfied
                break

        return old_min

    def min(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        return self.a[1]

    def size(self):
        return self.N

    def is_empty(self):
        return self.N == 0

    def is_full(self):
        return self.N == self.max
