# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/Optimization-From-Brute-Force-to-Dynamic-Programming-Explained!
# https://www.youtube.com/watch?v=cjWnW0hdF1Y

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        maximum = 1
        for i in range(n):
            for j in range(i+1):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
            maximum = max(maximum, dp[i])
        return maximum

# https://www.youtube.com/watch?v=cjWnW0hdF1Y
class Solution2:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        n = len(nums)
        maximum = 1
        for i in range(n- 1, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maximum = max(maximum, dp[i])
        return maximum

