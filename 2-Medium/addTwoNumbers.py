# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' inplace '''
        p1, p2, carry = l1, l2, 0
        while p1 or p2 or carry:
            if p2:
                p1.val += p2.val
                p2 = p2.next
            p1.val += carry
            p1.val, carry = p1.val % 10, p1.val // 10
            if not p1.next and (p2 or carry):
                p1.next = ListNode()
            p1 = p1.next
        return l1
