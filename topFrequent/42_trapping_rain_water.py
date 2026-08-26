class Solution:
    def trap(self, height: List[int]) -> int:
        lenHeight = len(height)
        leftMax = [0]*lenHeight
        rightMax = [0]*lenHeight

        for i in range(1, lenHeight):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        
        for i in range(lenHeight - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        

        sum = 0
        for i in range(lenHeight):
            sum += max(0, min(leftMax[i], rightMax[i]) - height[i])
        
        return sum
        
"""
source: neetcode

for a point, find its left max, its right side max, then minus the current height, if that is less than 0, then take it 0.
"""
        
