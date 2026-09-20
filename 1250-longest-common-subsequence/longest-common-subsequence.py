class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n= len(text1) #cols
        m = len(text2) #rows
        dp = [[0]*(n + 1) for i in range(m + 1)]

        print(dp)
        for i in range(1, m+1):
            for j in range(1, n + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
        return dp[-1][-1]
