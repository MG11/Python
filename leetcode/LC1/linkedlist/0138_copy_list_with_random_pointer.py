class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
    
        """
        1) create new node after every node, copy value and set pointers
        2) then set random in the newly created nodes
        3) then seperate the new nodes
        """
        if(not head):
            return head
        temp = head
        while(temp):
            newNode = Node(temp.val)
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next


        temp = head
        while(temp and temp.next):
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        newHead = head.next
        temp = head
        newNode = newHead

        while( newHead.next != None):
            temp.next = temp.next.next
            newHead.next = temp.next.next
            temp = temp.next
            newHead = newHead.next
        return newNode
