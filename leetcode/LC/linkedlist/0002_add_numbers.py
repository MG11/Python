from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(-1)
        head = dummy
        while(l1 or l2):
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            value = sum % 10  #reminder
            carry = sum // 10 if sum >= 10 else 0
            new_node = ListNode(value)
            head.next = new_node
            head = new_node
        if carry:
            new_node = ListNode(carry)
            head.next = new_node
            head = new_node
        return dummy.next
            