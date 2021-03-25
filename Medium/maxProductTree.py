#

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxProduct(root: TreeNode) -> int:

    sums = deque([])

    def sumTree(root):
        if not root:
            return 0
        sums.append(ans := root.val + sumTree(root.left) + sumTree(root.right))
        return ans

    total = sumTree(root)
    return max((x*(total-x) for x in sums)) % (10**9 + 7)


if __name__ == '__main__':
    temp = TreeNode()
    maxProduct(temp)
