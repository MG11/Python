# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

# https://leetcode.com/problems/binary-tree-right-side-view/discuss/56003/My-C%2B%2B-solution-modified-preorder-traversal

class Solution:
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
        