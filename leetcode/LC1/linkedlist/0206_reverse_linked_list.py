# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        prev = None
        
        while(current != None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def reverseRecursive(self, head):
        if(head.next == None):
            return head
        else:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head
            head.next = None
            return newHead
