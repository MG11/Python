from typing import List
# https://www.youtube.com/watch?v=I-l6PBeERuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        c = len(coins)
        dp = [[0 for i in range(amount+1)] for j in range(c +1)]
        dp[0][0] = 1
        # base case if no amount it can be made in one way
        # if no coins amount can be made in 0 ways
        for i in range(1,c+1):
            for j in range(amount+1):
                if(j == 0):
                    dp[i][j] = 1
                else:
                    if(coins[i-1] <=j):
                         # to count number of ways do +
                    # it is unbounded knapsack so do dp[i][j-coins[i-1]]
                        dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[c][amount]
    