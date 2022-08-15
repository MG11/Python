from typing import List

# https://leetcode.com/problems/permutations/solution/
class Solution:
    def __init__(self):
        self.res = []
    
    def backtracking(self, nums, index):
        if(index == len(nums) -1):
            self.res.append(nums[:])
        
        for x in range(index, len(nums)):
            nums[x], nums[index] = nums[index], nums[x]
            self.backtracking(nums, index+1)
            nums[x], nums[index] = nums[index], nums[x]
            
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.res
            