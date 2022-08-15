# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import defaultdict

# O(n) | O(log n)
class Solution:
    def inorder(self, root, data, level):
        if(root is None):
            return
        data[level] += root.val
        self.inorder(root.left, data, level+1)
        self.inorder(root.right, data, level+1)
        
        
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        data = defaultdict(int)
        self.inorder(root, data, 1)
        print(data)
        # the key whose value is the largest
        # key2 = max(square, key = lambda k: square[k])
        return max(data, key=lambda level: (data[level], -level))
    