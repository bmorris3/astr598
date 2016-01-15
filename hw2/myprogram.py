"""
ASTR 598 HW 2
Brett Morris
"""
from __future__ import print_function # Python 2 compatibility
from linkedlist import Node, LinkedList

# Create nodes to link

# Construct a linked list with them
ll = LinkedList(head=None, tail=None)

# Insert three new nodes at the head
nodes = [Node(data=i, next=None) for i in range(4)[::-1]]

for new_node in nodes:
    ll.insert_at_head(new_node)

# Delete the head node
old_head_data = ll.delete_at_head()

# Insert three new nodes at the tail
newer_nodes = [Node(data=i, next=None) for i in range(4, 8)]
for new_node in newer_nodes:
    ll.insert_at_tail(new_node)

print("Final contents of the linked list:", ll.traverse())
print("Old head, which has been deleted:", old_head_data)
