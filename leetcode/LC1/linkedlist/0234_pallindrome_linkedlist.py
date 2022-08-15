# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        counter = 0
        
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            counter += 1
        
        prev = None
        current = slow.next
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        temp = head
        while(prev):
            if(prev.val == temp.val):
                counter -=1
                prev = prev.next
                temp = temp.next
            else:
                return False
        return True
        
class Solution:
    def __init__(self):
        self.front_node = None
    
    def isPallindromeHelper(self, head: ListNode):
        if not head:
            return True
        if not self.isPallindromeHelper(head.next):
            return False
        if head.val != self.front_node.val:
            return False
        self.front_node = self.front_node.next
        return True
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_node = head
        return self.isPallindromeHelper(head) 
        
    