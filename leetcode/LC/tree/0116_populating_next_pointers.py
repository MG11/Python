class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# if left its next is node's left, if right and next right next is nodes's next's left
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(not root):
            return root
        
        temp = root
        
        if(temp.left):
            temp.left.next = temp.right
            
        if(temp.right and temp.next):
            temp.right.next = temp.next.left
        
        self.connect(temp.left)
        self.connect(temp.right)
        return root
