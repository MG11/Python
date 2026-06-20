# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    def reverseRecursive(self, head):
        if(head.next == None):
            return head
        else:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head
            head.next = None
            return newHead



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev

