from typing import List

# https://leetcode.com/problems/unique-paths-ii/

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


# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if( n== 0 or n == 1 or n == 2):
            return n
        
        secondLast = 1
        Last = 2
        current = 0
        for i in range(n-2):
            current = secondLast + Last
            secondLast = Last
            Last = current
        return current
        

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


# https://leetcode.com/problems/paint-house/

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0, 0, 0]
        
        for cost in costs:
            dp0 = cost[0] + min(dp[1], dp[2])
            dp1 = cost[1] + min(dp[0], dp[2])
            dp2 = cost[2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]
        return min(dp)


# https://leetcode.com/problems/decode-ways/

# recursion with memorization
# O(n) | O(n)
class Solution1:
    def __init__(self):
        self.memo = {} # key is index value is ans at that index
        
    def numDecodingsHelper(self, index, s):
        if(index == len(s)):
            return 1
        if(s[index] == '0'):
            return 0
        if(index == len(s) - 1):
            return 1
        if(self.memo.get(index)):
            return self.memo[index]
        
        ans = self.numDecodingsHelper(index + 1, s)
        if(int(s[index: index + 2]) <= 26):
            ans += self.numDecodingsHelper(index + 2, s)
        self.memo[index] = ans
        return ans
        
        
    def numDecodings(self, s: str) -> int:
        return self.numDecodingsHelper(0, s)

# DP
class Solution:
    def numDecodings(self, s: str) -> int:
        if not len(s):
            return 0
        if(s[0] == '0'):
            return 0
        if len(s) == 1:
            return 1
        dp = [0 for i in range(len(s))]
        # initialize last and second last values with the conditions
        dp[-1] = 1 if s[-1] != '0' else 0
        dp[-2] = 0 if s[-2] == '0' else dp[-1] if int(s[-2:]) > 26 else dp[-1] + 1
        for i in range(len(s) - 3,-1, -1):
            if(s[i] == '0'):
                dp[i] = 0
            elif(int(s[i:i+2]) > 26):
                dp[i] = dp[i+1]
            else:
                dp[i] = dp[i+1] + dp[i+2]
        return dp[0]

# https://leetcode.com/problems/maximal-square/
# traverse through matrix and update if current is 1 with min of all adjacent values + 1
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
   

 