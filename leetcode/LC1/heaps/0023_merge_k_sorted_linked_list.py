# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
take min heap, push elements of first index in the heap, take out one element each time and push next
"""

from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heaplist = []
        
        for key, value in enumerate(lists):
            if value:
                heapq.heappush(heaplist, (value.val, key))
        
        node = ListNode(-1)
        temp = node
        while len(heaplist):
            val, i = heapq.heappop(heaplist)
            currentnode = lists[i]
            lists[i] = lists[i].next
            node.next = currentnode
            node = node.next
            if currentnode.next is not None:
                heapq.heappush(heaplist, (currentnode.next.val, i))
        return temp.next
