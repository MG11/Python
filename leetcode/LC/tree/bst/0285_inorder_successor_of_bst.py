from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# also check
# https://www.geeksforgeeks.org/inorder-succesor-node-binary-tree/ reverse inorder traversal

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        successor = None
        
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
