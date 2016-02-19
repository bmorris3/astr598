"""
ASTR 598 HW 6
Brett Morris
"""


def mergesort(a):
    global b
    b = a[:]    # A slice is a copy
    result = _sort(a, 0, len(a)-1)
    return result


def _sort(a, low, high):
    # Catch base case
    if high <= low:
        return a

    mid = low + (high - low) // 2
    left_half_sorted = _sort(a, low, mid)       # sort left-half
    both_sorted = _sort(left_half_sorted, mid+1, high)    # sort right-half
    result = _merge(both_sorted, low, mid, high)
    return result


def _merge(a, low, mid, high):
    i = low
    j = mid + 1

    k = low
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            b[k] = a[j]
            k += 1
            j += 1

    while i <= mid:
        b[k] = a[i]
        k += 1
        i += 1

    while j <= high:
        b[k] = a[j]
        j += 1
        k += 1

    for i in range(low, high+1):
        a[i] = b[i]
    return a