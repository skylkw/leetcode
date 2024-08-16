# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            num = sum % 10
            carry = sum // 10
            new_node = ListNode(num)
            cur.next = new_node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            num = sum % 10
            carry = sum // 10
            new_node = ListNode(num)
            cur.next = new_node
            cur = cur.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            num = sum % 10
            carry = sum // 10
            new_node = ListNode(num)
            cur.next = new_node
            cur = cur.next
            l2 = l2.next
        if carry == 1:
            cur.next = ListNode(1)

        return dummy.next
