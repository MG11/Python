from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
O(n) | O(logn)

# LC 979
"""

class Solution:
    def distributeCoinsHelper(self, root, moves):
        if(root is None):
            return 0
        left = self.distributeCoinsHelper(root.left, moves)
        right = self.distributeCoinsHelper(root.right, moves)
        moves[0] += abs(left) + abs(right)
        return root.val + left + right - 1
        
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = [0]
        self.distributeCoinsHelper(root, moves)
        return moves[0]
        