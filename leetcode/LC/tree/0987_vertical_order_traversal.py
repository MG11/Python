# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/565677/Python-Using-Dictionary-Beats-98
https://practice.geeksforgeeks.org/problems/vertical-sum/1
https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
"""

from typing import Optional, List
from collections import defaultdict
# O(nlogn) | O(n), dfs using preorder traversal
class Solution:
    def verticalTraversalHelper(self, root, data, row, column):
        if(root is None):
            return
        data[column].append((row, root.val))
        self.verticalTraversalHelper(root.left, data, row+1, column-1)
        self.verticalTraversalHelper(root.right, data, row+1, column+1)
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = defaultdict(list)
        ans = []
        self.verticalTraversalHelper(root, data, 0, 0)
        
        for d in sorted(data.keys()):
            temp = []
            for j in sorted(data[d]):
                temp.append(j[1])
            ans.append(temp)
        return ans
