import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        maxsum = nums[0]

        for i in nums[1:]:
            if cursum < 0:
                cursum = 0

            cursum += i
            if cursum > maxsum:
                maxsum = cursum

        if maxsum <= 0:
            return max(nums)
        return maxsum
