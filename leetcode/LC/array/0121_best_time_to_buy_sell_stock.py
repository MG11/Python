from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = float('inf')
        
        for price in prices:
            if minimum > price:
                minimum = price
            currentProfit = price - minimum
            profit = max(currentProfit, profit)
        return profit
        