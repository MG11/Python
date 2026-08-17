from typing import List

"""
ex
[1, 2, 3, 4]
left: [1, 1, 1*2, 1*2*2]
right: [2*3*4,3*4,4,1] i.e 2*3*4 is formed by multiplying 2 (nums[1] ) and next output. 
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        
        left = 1
        for i in range(0, len(nums)):
            if i > 0:
                left = left *nums[i-1]
            output[i] = left
        
        right = 1
        for i in range(len(nums) -1, -1, -1):
            if i < len(nums) - 1:
                right = right*nums[i+1]
            output[i] *= right
        return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lefttoRight = [1]*len(nums)
        righttoLeft = [1]*len(nums)

        for i in range(1, len(lefttoRight)):
            lefttoRight[i] = nums[i-1]*lefttoRight[i-1]
        
        for i in range(len(righttoLeft) - 2, -1, -1):
            righttoLeft[i] = nums[i+1]*righttoLeft[i+1]
        
        return [righttoLeft[i]*lefttoRight[i] for i in range(len(nums))]

        
