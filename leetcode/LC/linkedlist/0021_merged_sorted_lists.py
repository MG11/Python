# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(ans, l1):
            node = ListNode(l1.val)
            l1 = l1.next
            ans.next = node
            ans = ans.next
            return ans, l1
        
        ans = ListNode()
        temp = ans
        
        while(l1 and l2):
            if(l1.val >= l2.val):
                ans, l2 = merge(ans, l2)
            elif(l1.val < l2.val):
                ans, l1 = merge(ans, l1)
    
        while l1:
            ans, l1 = merge(ans, l1)
        while l2:
            ans, l2 = merge(ans, l2)
        return temp.next
