from LinkedListBuilder import ListNode, ListNodeBuilder
import heapq

''' Not sure how to implement the optimal merge sort in this '''

''' Technically this is an O(n) operation as well, debately better than a merge sort since a list insertion is O(n) in python'''


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return
        pool = []
        for node in lists:
            while node:
                heapq.heappush(pool, node.val)
                node = node.next
        if not pool:
            return
        head = pointer = ListNode()
        for _ in range(len(pool)-1):
            pointer.val, pointer.next = heapq.heappop(pool), ListNode()
            pointer = pointer.next
        else:
            pointer.val = pool[-1]
        return head

    def mergeKListsLazy(self, lists: list[ListNode]) -> ListNode:
        pool = []
        for node in lists:
            while node:
                pool.append(node.val)
                node = node.next
        pool.sort()
        return ListNodeBuilder(pool).head
