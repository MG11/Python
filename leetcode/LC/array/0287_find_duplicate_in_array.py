"""
1) sort,
2) set
3) use floyd cycle detection algo, O(n)| O(1)
"""
from typing import List

class Solution:
    def detectCycle(self, nums):
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow == fast):
                return slow
        
        
    def findDuplicate(self, nums: List[int]) -> int:
        
        meet = self.detectCycle(nums)
        start = nums[0]
        while(start != meet):
            start = nums[start]
            meet = nums[meet]
        return start
        