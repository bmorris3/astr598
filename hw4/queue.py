"""
ASTR 598 HW 4
Brett Morris
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self, head=None, tail=None):
        """
        Construct a Queue object
        """
        self.head = head
        self.tail = tail
        self.N = 0          # Size of the stack

    def put(self, i):

        if self.N == 0:
            self.head = Node(data=i, next=None)
            self.tail = self.head
        elif self.head == self.tail:
            new_tail = Node(data=i, next=None)
            self.head.next = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(data=i, next=None)
            self.tail.next = new_tail
            self.tail = new_tail

        self.N += 1

    def get(self):
        if self.N == 0:
            raise IOError('Stack is empty')
        else:
            popped_integer = self.head.data

        new_head = self.head.next
        self.head = new_head
        self.N -= 1
        return popped_integer

    def front(self):
        return self.head.data

    def size(self):
        return self.N

    def is_empty(self):
        return self.N == 0
