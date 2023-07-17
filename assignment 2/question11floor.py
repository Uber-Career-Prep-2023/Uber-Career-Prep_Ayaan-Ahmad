class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_floor(root, target):
    floor = None

    while root:
        if root.val == target:
            return root.val
        elif root.val < target:
            floor = root.val
            root = root.right
        else:
            root = root.left

    return floor