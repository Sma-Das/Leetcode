"""
Focus was on optimisation of the problem. Although it should maybe sneak into an easy medium

83.77% // 71.05%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack, values = [root], []
        while stack:
            curr = stack.pop()
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
            bisect.insort(values, curr.val)
        new_root = pointer = TreeNode()
        for val in values[:-1]:
            pointer.val, pointer.right = val, TreeNode()
            pointer = pointer.right
        pointer.val = values[-1]
        return new_root
