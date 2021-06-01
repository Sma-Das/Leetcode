class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(r: TreeNode) -> int:
        def t(r, x, i): return max(t(r.left, max(x, r.val), min(i, r.val)), t(
            r.right, max(x, r.val), min(i, r.val))) if r else x - i
        return t(r, 0, 100000)
