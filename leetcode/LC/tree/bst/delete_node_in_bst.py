# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
class Solution:

    def successor(self, root, key):
        root = root.right
        while root.left:
            root = root.left
        return root
    
    def precedor(self, root, key):
        root = root.left
        while root.right:
            root = root.right
        return root
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right:
                p = self.successor(root, key)
                root.val = p.val
                root.right = self.deleteNode(root.right, p.val)
            elif root.left:
                s = self.precedor(root, key)
                root.val = s.val
                root.right = self.deleteNode(root.left, s.val)
            else:
                return None
        return root
