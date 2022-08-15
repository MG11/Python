# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        even = head.next if head.next else None
        even_start = even
        while(even and even.next):
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = even.next

           
        odd.next = even_start
        return head
        