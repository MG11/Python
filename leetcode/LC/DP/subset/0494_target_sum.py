class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target + sum(nums)) % 2 != 0:
            return 0
        target = (target + sum(nums)) // 2
        if target < 0:
            return 0
        dp = [[1] + [0]*(target) for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            for j in range(0, target + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][target]
