class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        return self._find_min(self.root)

    def max(self):
        return self._find_max(self.root)

    def contains(self, val):
        return self._contains(self.root, val)

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.val

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node.val

    def _contains(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._contains(node.left, val)
        else:
            return self._contains(node.right, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def _delete(self, node, val):
        if not node:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: Get the inorder successor
            temp_val = self._find_min(node.right)

            # Delete the inorder successor
            node.right = self._delete(node.right, temp_val)

            # Copy the inorder successor's value to this node
            node.val = temp_val

        return node



test = BinarySearchTree()
