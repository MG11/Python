from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for i in nums:
            total += i
        
        if(total % 2 != 0):
            return False
        total = total//2
        
        dp = [0 for i in range(total+1)]
        dp[0] = 1
        
        for i in range(len(nums)):
            for j in range(total, -1, -1):
                if(nums[i] <= j):
                    dp[j] = dp[j] or dp[j-nums[i]]
        return dp[total]
        