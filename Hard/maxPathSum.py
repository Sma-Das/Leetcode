"""
One of the most enjoyable hard questions on Leetcode.
A really hard problem until you break it down into smaller subproblems
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode) -> int:
    ans = -float('inf')

    def find_max(node):
        nonlocal ans
        if not node:
            return 0
        left, right = find_max(node.left), find_max(node.right)
        closed_loop = max(node.val, node.val + max(left, right))
        ans = max(ans, closed_loop, left + node.val + right)
        return closed_loop

    find_max(root)
    return ans
