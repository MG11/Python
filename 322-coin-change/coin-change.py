class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[-1] if dp[-1] <= amount else -1

