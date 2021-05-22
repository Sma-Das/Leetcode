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
        closed_loop = max(node.val,
                          node.val + max(l := find_max(node.left), r := find_max(node.right)))
        ans = max(ans, closed_loop, l + node.val + r)
        return closed_loop

    find_max(root)
    return ans
