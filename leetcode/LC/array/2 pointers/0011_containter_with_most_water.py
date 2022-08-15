"""
if some maxarea simultaneously, 
if height[left] is higher consider that else consider right height for next operation
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        
        while(left < right):
            distance = right - left
            maxarea = max(maxarea, distance*min(height[left], height[right]))
            if(height[left] > height[right]):
                right -=1
            else:
                left += 1
        return maxarea
        