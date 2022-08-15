from typing import List

#  https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [0 for i in range(col+1)]
        for r in range(row):
            for c in range(col):
                # if it is first row just add previous dp value
                if not r:
                    dp[c + 1] = grid[r][c] + dp[c]
                # if it is first column just add current grid value
                elif not c:
                    dp[c + 1] += grid[r][c]
                # take min of value at one row less and one col less, + current grid value
                else:
                    dp[c+1] = min(dp[c+1], dp[c]) + grid[r][c]
        return dp[col]
