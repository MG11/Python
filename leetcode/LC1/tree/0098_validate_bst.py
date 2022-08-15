from typing import Optional
import sys

#  can also do inorder traversal of the tree check if current value is greater than previous

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def isValidBSTHelper(self, root, max_value, min_value):
        if(not root):
            return True
        if(min_value < root.val < max_value):
            return self.isValidBSTHelper(root.left, root.val, min_value ) and self.isValidBSTHelper(root.right, max_value, root.val)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, sys.maxsize, -sys.maxsize)
    