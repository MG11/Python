class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        n = len(nums)
        maximum = 1
        for i in range(n- 1, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maximum = max(maximum, dp[i])
        print(dp)
        return maximum
