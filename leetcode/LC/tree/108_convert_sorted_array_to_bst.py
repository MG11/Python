from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertArrayToBSTHelper(self, nums, start, end):
        if(start > end):
            return None
        
        mid = (start + end)//2
        
        node = TreeNode(nums[mid])
        node.left = self.convertArrayToBSTHelper(nums, start, mid-1)
        node.right = self.convertArrayToBSTHelper(nums, mid+1, end)
        return node
        
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.convertArrayToBSTHelper(nums, 0, len(nums) - 1)
        