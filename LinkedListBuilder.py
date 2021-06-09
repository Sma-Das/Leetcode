class ListNode:
    ''' Basic linked list implementation '''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        pointer, output = self, ""
        while pointer:
            output, pointer = output + f"{pointer.val} -> ", pointer.next
        return output[:-3].rstrip()


class ListNodeBuilder:
    def __init__(self, iterable: iter):
        if not (isinstance(iterable, type(iter)) or hasattr(iterable, "__iter__")):
            raise TypeError("Give value is not iterable")
        self.head = self.build_list(iter(iterable))
        self.iterable = iterable  # In case you want to retain the original iterable

    def build_list(self, iterable: iter = None) -> LinkedList:
        if iterable is None:
            iterable = self.iterable
        head = pointer = LinkedList()
        while pointer:
            pointer.val, pointer.next = next(iterable, None), LinkedList()
            if pointer.val is None:
                break
            pointer = pointer.next
        pointer.next = None
        return head
