from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def dfs(row, col, direction):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if not grid[row][col] or (row, col) in seen:
                return
            seen.add((row, col))
            path.append(direction)
            dfs(row + 1, col, "D")
            dfs(row - 1, col, "U")
            dfs(row, col + 1, "R")
            dfs(row, col - 1, "L")
            path.append("0")  
        seen = set()
        unique_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                path = []
                dfs(i, j,"0")
                if path:
                    unique_islands.add(''.join(path))
        print(unique_islands)
        return len(unique_islands)    
