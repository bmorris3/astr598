"""
ASTR 598 HW 7
Brett Morris
"""

__all__ = ['BinarySearchTree']

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root
        self.N = 0

    def insert(self, i):
        node = Node(i, left=None, right=None)

        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, local_root=None, node=None):
        if local_root is None:
            raise ValueError("No local root.")

        self.N += 1

        # Recursively walk down the tree and insert at a terminus
        if node.data < local_root.data:
            if local_root.left is None:
                local_root.left = node
            else:
                self._insert(local_root.left, node)
        else:
            if local_root.right is None:
                local_root.right = node
            else:
                self._insert(local_root.right, node)

    def find(self, i):
        return self._find(i)

    def _find(self, local_root=None, i=None):
        if local_root is None:
            return False
        elif local_root.data == i:
            return True
        elif i < local_root.data:
            return self._find(local_root.left, i)
        else:
            return self._find(local_root.right, i)

    def traverse_pre_order(self):
        self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, local_root=None):
        if local_root is None:
            return
        else:
            print(local_root.data)
            self._traverse_pre_order(local_root.left)
            self._traverse_pre_order(local_root.right)

    def traverse_in_order(self):
        self._traverse_in_order(self.root)

    def _traverse_in_order(self, local_root=None):
        if local_root is None:
            return
        else:
            self._traverse_in_order(local_root.left)
            print(local_root.data)
            self._traverse_in_order(local_root.right)

    def traverse_post_order(self):
        self._traverse_post_order(self.root)

    def _traverse_post_order(self, local_root=None):
        if local_root is None:
            return
        else:
            self._traverse_post_order(local_root.left)
            self._traverse_post_order(local_root.right)
            print(local_root.data)

    def traverse(self):
        return self.traverse_in_order()

    def max(self):
        if self.root is None:
            raise ValueError('Empty tree.')

        local_root = self.root
        i = local_root.data

        while local_root is not None:
            i = local_root.data
            local_root = local_root.right

        return i
    def min(self):
        if self.root is None:
            raise ValueError('Empty tree.')

        local_root = self.root
        i = local_root.data

        while local_root is not None:
            i = local_root.data
            local_root = local_root.left

        return i

    def size(self):
        return self.N

