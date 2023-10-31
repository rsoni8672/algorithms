from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_pointer = head.next
        back_pointer = head
        if first_pointer is None:
            return back_pointer

        temp = first_pointer.next

        while temp is not None:
            temp = first_pointer.next
            first_pointer.next = back_pointer
            back_pointer = back_pointer.next
        return first_pointer



