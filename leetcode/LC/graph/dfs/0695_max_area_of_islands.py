# O(m*n) | O(m*n) the total number of squares explored will be the area of that connected shape.
from typing import List

class Solution:
    
    def dfs(self, grid, r, c):
        if(grid[r][c] == 0):
            return 0
        grid[r][c] = 0
        area = 1
        directions = [(r+1, c) , (r, c+1), (r-1, c), (r, c-1)]
        for direction in directions:
            if((0 <= direction[0] < len(grid)) and (0 <= direction[1] < len(grid[0]))):
                # print(direction)
                area += self.dfs(grid, direction[0], direction[1])
        return area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                current_area = self.dfs(grid, r, c)
                max_area = max(max_area, current_area)
        return max_area
        