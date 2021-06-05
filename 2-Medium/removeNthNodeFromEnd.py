# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    ''' 92.22% // 75.79% '''

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        {(fast := fast.next) for _ in range(n)}
        if fast is None:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
