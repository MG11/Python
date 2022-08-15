# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
also can be done recursively, if they are symatric mirror will be same 
"""

from typing import Optional, List
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        
        # if root is not there
        if(not root):
            return True
        # if only root is there
        if(root.left is None and root.right is None):
            return True
        
        # compare root left and right values
        if(root.left is not None and root.right is not None and root.left.val == root.right.val):
            dq.append((root.left, root.right))
        else:
            return False
        
        
        # compare left's right and right's left also left's left and right'right
        while(len(dq)):
            
            e1 = dq.popleft()
            if(not e1[0] and not e1[1]):
                continue
            
            if(not e1[0] or not e1[1]):
                return False
            
            if(e1[0].val != e1[1].val):
                return False
            
            dq.append((e1[0].right, e1[1].left))
            dq.append((e1[0].left, e1[1].right))
        return True


# https://leetcode.com/problems/binary-tree-right-side-view/
class Solution2:
    def rightSideViewHelper(self, root, right_view, startlevel):
        if(not root):
            return
        if(startlevel == len(right_view)):
            right_view.append(root.val)
        
        self.rightSideViewHelper(root.right, right_view, startlevel+1)
        self.rightSideViewHelper(root.left, right_view, startlevel+1)
        
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        self.rightSideViewHelper(root, right_view, 0)
        return right_view
        

