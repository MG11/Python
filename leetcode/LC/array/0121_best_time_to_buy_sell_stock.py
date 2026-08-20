"""
[7 , 1, 5, 3, 6, 4]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        maximum = 0

        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                maximum = max(maximum, prices[i] - minimum)
        return maximum
