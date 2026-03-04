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
 


class Solution1:
    def __init__(self):
        self.board = []

    def checkIsland(self, r, c):
        if self.board[r][c] == "0" or self.board[r][c] == "#":
            return 0
        
        self.board[r][c] = "#"
        directions = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]

        for direction in directions:
            if direction[0] < len(self.board) and direction[1] < len(self.board[0]) and direction[0] >= 0 and direction[1] >= 0:
                self.checkIsland(direction[0], direction[1])
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.board = grid
        numberOfIsland = 0
        for r in range(rows):
            for c in range(cols):
                island = self.checkIsland(r, c)
                numberOfIsland += island
        return numberOfIsland

