from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
