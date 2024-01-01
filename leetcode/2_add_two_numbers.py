from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        output = None
        head = None
        while l1 is not None or l2 is not None:
            left_bit = 0
            right_bit = 0

            if l1 is not None:
                left_bit = l1.val
            if l2 is not None:
                right_bit = l2.val
            bit_sum = ListNode((left_bit + right_bit + carry) % 10)
            carry = (left_bit + right_bit + carry) // 10

            if output is None:
                output = bit_sum
                head = output
            else:
                output.next = bit_sum
                output = bit_sum
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            output.next = ListNode(carry)
        return head
