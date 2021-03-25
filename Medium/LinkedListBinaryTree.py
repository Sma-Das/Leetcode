# 96ms 89.47%


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    ''' Definition for a binary tree node.'''

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubPath(head: ListNode, root: TreeNode) -> bool:
    if not root:
        return False
    elif root.val == head.val and traverseDown(head, root):
        return True
    else:
        return isSubPath(head, root.left) or isSubPath(head, root.right)


def traverseDown(head, root):
    if not head:
        return True
    elif not root:
        return False
    elif root.val == head.val:
        return traverseDown(head.next, root.left) or traverseDown(head.next, root.right)
    else:
        return False
    return True
