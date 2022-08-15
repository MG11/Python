from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        i = 0
        while(i < len(heights)):
            if(not len(stack) or heights[stack[-1]] <= heights[i]):
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                area = heights[tp]*(i if not len(stack) else (i - stack[-1] -1))
                maxarea = max(area, maxarea)
        
        while(len(stack)):
            tp = stack.pop()
            area = heights[tp]*(i if not len(stack) else (i - stack[-1] -1))
            maxarea = max(area, maxarea)
        return maxarea
