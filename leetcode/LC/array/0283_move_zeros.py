"""
take position of last non zero element to be inserted.
and insert non zero elements..

after that fill rest of the part with 0 elements..
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lastoccurance = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastoccurance] = nums[i]
                lastoccurance += 1
        
        for i in range(lastoccurance, len(nums)):
            nums[i] = 0
        return nums
