class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        
        for i in range(0,m):
            for j in range(1, n+1):
                dp[j] += dp[j-1]
        return dp[-1]


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
