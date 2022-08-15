from typing import Optional
import sys

# https://www.youtube.com/watch?v=Osz-Vwer6rw

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSumHelper(self, root, sum):
        if root is None:
            return 0
        
        l = self.maxPathSumHelper(root.left, sum)
        r = self.maxPathSumHelper(root.right, sum)
        l = max(l,0)
        r = max(r, 0)
        
        # current root node both childen not to be taken in path
        temp = max(l + root.val, r + root.val)
        
        # current root node both children to be taken in path
        ans = max(temp, l + r + root.val)
        
        sum[0] = max(sum[0], ans)
        return temp
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sum = [-sys.maxsize]
        self.maxPathSumHelper(root, sum)
        return sum[0]
