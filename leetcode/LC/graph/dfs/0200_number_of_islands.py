from typing import List

# O(m*n) | O(m*n)

class Solution:
    def dfs(self, grid, r, c):
        if(grid[r][c] == '0'):
            return 0
        grid[r][c] = '0'
        area = 1
        directions = [(r+1, c) , (r, c+1), (r-1, c), (r, c-1)]
        for direction in directions:
            if((0 <= direction[0] < len(grid)) and (0 <= direction[1] < len(grid[0]))):
                area += self.dfs(grid, direction[0], direction[1])
                # print(grid)
        area = 1 if area > 0 else 0
        return area
    
    def numIslands(self, grid: List[List[str]]) -> int:
        number_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                island_count = self.dfs(grid, r, c)
                number_island += island_count
        return number_island
 

