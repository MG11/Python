from typing import List

# O(n) | O(1) 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        ans = []
        while(start <= end):
            if abs(nums[start]) > abs(nums[end]):
               ans.append(nums[start]**2)
               start += 1
            else:
               ans.append(nums[end]**2)
               end -= 1
        ans.reverse() # reverses in place, O(n)
        return ans
        
        