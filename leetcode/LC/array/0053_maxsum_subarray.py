from typing import List

# O(n) | O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = -float('inf')
        
        for num in nums:
            sum += num
            if (sum > maxsum):
                maxsum = sum
                
            # change sum after evaluating maximum
            if(sum < 0):
                sum = 0
        
        # if maxsum is negative, return maximum value
        maxsum = max(nums) if maxsum < 0 else maxsum
        return maxsum
