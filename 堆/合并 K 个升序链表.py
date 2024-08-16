# Definition for singly-linked list.
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ListNode.__lt__ = lambda a, b: a.val < b.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [head for head in lists if head]
        heapq.heapify(min_heap)

        dummy = ListNode()
        cur = dummy
        while min_heap:
            min_node = heapq.heappop(min_heap)
            cur.next = min_node
            cur = cur.next
            if min_node.next:
                heapq.heappush(min_heap, min_node.next)
        return dummy.next
