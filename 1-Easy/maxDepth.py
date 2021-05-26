class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode, count: int = 0):
    if root is None:
        return count
    return max(maxDepth(root.left, count+1), maxDepth(root.right, count+1))
