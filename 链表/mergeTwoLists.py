# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        list = head

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                list.next = list1
                list1 = list1.next
            else:
                list.next = list2
                list2 = list2.next
            list = list.next

        if list1 is not None:
            list.next = list1
        if list2 is not None:
            list.next = list2
        return head.next
