class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode, lo=float('-inf'), hi=float('inf')):
    if not root:
        return True
    if root.val >= hi or root.val <= lo:
        return False
    return isValidBST(root.left, lo, root.val) and isValidBST(root.right, root.val, hi)
