class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        left = [0] * n
        right = [0] * n

        left[0]=height[0]
        right[n-1] = height[n-1]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        max_amount = 0
        for i in range(n):
            max_amount += min(left[i], right[i]) - height[i]
        return max_amount
        
"""
source: neetcode

for a point, find its left max, its right side max, then minus the current height, if that is less than 0, then take it 0.
"""
        
