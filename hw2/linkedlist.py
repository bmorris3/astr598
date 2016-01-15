"""
ASTR 598 HW 2
Brett Morris
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        if ((head is not None and tail is not None) or
           (head is None and tail is None)):
            self.head = head
            self.tail = tail
        elif head is not None and tail is None:
            self.head = head
            self.tail = head
        else:
            self.head = None
            self.tail = None

    def insert_at_head(self, new_head_node):
        old_head = self.head
        self.head = new_head_node
        self.head.next = old_head

        if old_head == self.tail or self.tail is None:
            self.tail = self.head.next

    def delete_at_head(self):
        if self.head.next is not None:
            old_head = self.head
            new_head = self.head.next
            self.head = new_head

            # Return the data from the old head node
            return old_head.data
        else:
            raise ValueError('Head cannot be deleted.')

    def delete_at_tail(self):
        """
        I've implemented this function for educational purposes.
        I demonstrate here that you need to traverse the entire list
        to find the tail node and delete it.
        """
        old_tail = self.tail

        # After this loop, node_i will be the second to last node
        node_i = self.head
        while node_i.next.next is not None:
            node_i = node_i.next

        # Make the second to last node the tail node
        self.tail = node_i
        node_i.next = None

        # Return the data from the old tail node
        return old_tail.data

    def insert_at_tail(self, new_node):
        if self.tail is not None:
            # Reset the next attribute of the current tail to the new node
            self.tail.next = new_node
            # Make the new tail the new node
            self.tail = new_node

        elif self.head == self.tail:
            self.tail = self.head.next

    def traverse(self):
        """
        Traverse the linked list, return a Python `list` of the data values
        at each node, in order.
        """
        traversed_list = []
        node_i = self.head
        while node_i.next is not None:
            traversed_list.append(node_i.data)
            node_i = node_i.next
        else:
            # Include the last node
            traversed_list.append(node_i.data)

        return traversed_list

    def __repr__(self):
        return "<Linked list: "+str(self.traverse())+">"
