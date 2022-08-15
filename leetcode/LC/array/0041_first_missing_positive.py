from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        
        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = length + 1
        
        for i in range(length):
            if abs(nums[i]) == length + 1:
                continue
            num = abs(nums[i])
            num -= 1
            if(nums[num] > 0):
                nums[num] = -1*nums[num]
        
        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1
