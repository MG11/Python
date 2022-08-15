from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        dp = [0 for i in range(col+1)]
        dp[1] = 1 if not obstacleGrid[0][0] else 0
    
        for r in range(row):
            for c in range(col):
                if(not obstacleGrid[r][c]):
                    dp[c+1] += dp[c]
                else:
                    dp[c+1] = 0
        return dp[col]
