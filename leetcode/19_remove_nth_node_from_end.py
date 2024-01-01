from typing import Optional

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front_pointer = head
        back_pointer =  head
        for counter in range(n):
            front_pointer = front_pointer.next

        while front_pointer is not None:
            back_pointer = back_pointer.next
            front_pointer = front_pointer.next

        back_pointer.next = back_pointer.next.next

        return head

