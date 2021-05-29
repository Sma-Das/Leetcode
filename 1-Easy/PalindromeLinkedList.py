"""
71.86% Speed and 39.97% Memory

O(n) // O(n) can be optimised to O(n) // O(1) by using a fast and slow pointer
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes == nodes[::-1]
