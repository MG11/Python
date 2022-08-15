from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(col)] for i in range(row)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if(i and j and dp[i][j]):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j])
        return ans*ans
   