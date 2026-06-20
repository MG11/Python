# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(-1, head)
        left, right = prev, prev

        while n and right.next:
            right = right.next
            n -= 1
        
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next if left.next else None

        return prev.next
