# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_1 = ListNode()
        dummy_2 = ListNode()
        cur = head
        dummy_1_head = dummy_1
        dummy_2_head = dummy_2
        while cur:
            if cur.val < x:
                dummy_1.next = cur
                dummy_1 = dummy_1.next
            else:
                dummy_2.next = cur
                dummy_2 = dummy_2.next
            cur = cur.next
        dummy_2.next = None
        dummy_1.next = dummy_2_head.next
    
        return dummy_1_head.next
