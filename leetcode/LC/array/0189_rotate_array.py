"""
reverse complete arrray, then reverse first part and then second part, O(n) |O(1)
brute force:
1) use extra space of O(n),
2) reverse k times, so, complexity becomes O(kn)
"""
from typing import List

class Solution:
    def reverse(self, nums, start, end):
        while(start <= end):
            c = nums[end]
            nums[end] = nums[start]
            nums[start] = c
            start += 1
            end -= 1
        
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        self.reverse(nums, 0, l-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, l-1)
        
        