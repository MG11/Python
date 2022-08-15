# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   
"""
O(n) | O(n) ( used to create map)
"""

from typing import List, Optional

class Solution:
    prestart = 0
    def buildTreeHelper(self, preorder, start, end, inorder_dict):
        if(start > end):
            return None
        current_element = preorder[self.prestart]
        self.prestart += 1
        root = TreeNode(current_element)
        inorder_position = inorder_dict[current_element]
        root.left = self.buildTreeHelper(preorder, start, inorder_position - 1, inorder_dict)
        root.right = self.buildTreeHelper(preorder, inorder_position+1, end, inorder_dict)
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        for i in range(0, len(inorder)):
            inorder_dict[inorder[i]] = i

        return self.buildTreeHelper(preorder, 0, len(inorder) - 1, inorder_dict)


# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution:
    def __init__(self):
        self.postend = 0
    
    def buildTreeHelper(self, postorder, start, end, inorder_dict):
        if(start > end):
            return None
        root = TreeNode(postorder[self.postend])
        self.postend -= 1
        inindex = inorder_dict[root.val]
        root.right = self.buildTreeHelper(postorder, inindex+1, end, inorder_dict)
        root.left = self.buildTreeHelper(postorder, start, inindex-1, inorder_dict)
        return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postend = len(postorder) - 1
        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i        
        return self.buildTreeHelper(postorder, 0, len(inorder) -1, inorder_dict)


# https://www.geeksforgeeks.org/construct-tree-inorder-level-order-traversals-set-2/
class Solution:

    def __init__(self) -> None:
        self.map = {}
    
    def buildTreeHelper(self, inorder, levelorder, start, end):
        if start > end:
            return None
        
        mid_index = start

        for i in range(start, end +1):
            if self.map.get(inorder[i] < self.map.get(inorder[mid_index])):
                mid_index = i
        
        root = TreeNode(inorder[mid_index])

        root.left = self.buildTreeHelper(inorder, levelorder, 0, mid_index-1)
        root.right = self.buildTreeHelper(inorder, levelorder, mid_index+1, end)
        return root


    def buildTree(self, inorder, levelorder):
        
        for i in range(len(levelorder)):
            self.map[i] = i
        start = 0
        end = len(inorder) - 1
        self.buildTreeHelper(inorder, levelorder, start, end)
