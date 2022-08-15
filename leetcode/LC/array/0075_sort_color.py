from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) < 2):
            return
        start = 0
        end = 0


        while( end < len(nums)):
            if nums[start] != 0:
                while(nums[end] != 0 and end < len(nums) -1):
                    end += 1
                if(nums[end] == 0):
                    nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end += 1
            
        end = len(nums) - 1
        start = len(nums) - 1
        while(end >= 0):
            if nums[start] != 2:
                while(nums[end] != 2 and end > 0):
                    end -= 1
                if(nums[end] == 2):
                    nums[start], nums[end] = nums[end], nums[start]
            start -= 1
            end -= 1
            