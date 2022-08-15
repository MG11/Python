# https://www.youtube.com/watch?v=I-l6PBeERuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16

# https://leetcode.com/problems/coin-change/discuss/77360/C%2B%2B-O(n*amount)-time-O(amount)-space-DP-solution
# use top down in unbounded, bottom up in 0-1 knapsack problem

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        c = len(coins)
#         initialize the dp with amount +1 as it can be the maximum amount
        dp = [amount +1 for i in range(amount+1)]
#        if amount is 0 there are 0 ways
        dp[0] = 0
    
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if(coins[i] <= j):
#                     +1 because the coin is used once,
# also the same coin can be used multiple times so, cut coin amount from the same row
# min of not taking this coin and taking this coin
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] <=amount else -1
        