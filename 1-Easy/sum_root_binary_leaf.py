class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        def traverse(head, total = 0):
            if not head:
                return total
            total = (total << 1) + head.val
            return traverse(head.left, total) + traverse(head.right, total)
        return traverse(root) >> 1
