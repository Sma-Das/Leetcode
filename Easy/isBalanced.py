class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:

    def check(root):
        if not root:
            return 0
        l, r = check(root.left), check(root.right)
        if -1 in [l, r] or abs(l-r) > 1:
            return -1
        return 1 + max(l, r)

    return not check(root) == -1
