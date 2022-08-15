from typing import Optional

# https://www.youtube.com/watch?v=LCRGV8avvUY

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        prev = None
        current = head
        
        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        
        l = length // k
        
        while(n < l):
            m = 0
            dummy = current
            dummy1 = prev
            while m <k:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                m += 1
            if (n == 0):
                head = prev
            dummy.next = current
            if dummy1:
                dummy1.next = prev
            prev = dummy
            n += 1
        return head
        