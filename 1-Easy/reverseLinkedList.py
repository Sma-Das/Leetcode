class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head) -> ListNode:
        """
        Inplace solution to the classic linked list problem
        """
        if not head:
            return head
        
        prev = None
        nxt = pointer = head
        
        while pointer.next is not None:
            pointer.next, nxt = prev, pointer.next
            prev = pointer
            pointer = nxt
        else:
            pointer.next = prev
            
        return pointer


def build_linked_list(values: list) -> ListNode:
    if not values:
        return

    head = pointer = ListNode()
    length = len(values)

    for i, value in enumerate(values):
        pointer.val = value
        if i < length - 1:
            pointer.next = ListNode()
        pointer = pointer.next

    return head
        

def print_linked_list(head: ListNode, arrow: str = " ->"):
    pointer = head
    linked_list = ""
    while pointer is not None:
        linked_list += pointer.val.__str__() + arrow
    
    print(linked_list.rstrip(arrow))
