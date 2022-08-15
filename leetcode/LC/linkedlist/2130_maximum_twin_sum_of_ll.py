# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def __init__(self):
        self.maximum = 0
        self.node = None
    
    def pairSumHelper(self, head):
        if( not head):
            return
        
        self.pairSumHelper(head.next)
        self.maximum = max(self.maximum, head.val + self.node.val)
        self.node = self.node.next
            
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        if(not head):
            return self.maximum
        self.node = head
        self.pairSumHelper(head)
        return self.maximum
