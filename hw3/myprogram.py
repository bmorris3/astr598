"""
ASTR 598 HW 3
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility
from stack import Stack

ten_integers = range(10)

mystack = Stack()

# Push ten integers to the stack:
for integer in ten_integers:
    mystack.push(integer)

print("What is top now?: {0}".format(mystack.top()))

# Pop ten integers from the stack:
for _ in ten_integers:
    print(mystack.pop())

print("Is stack empty now?: {0}".format(mystack.is_empty()))
