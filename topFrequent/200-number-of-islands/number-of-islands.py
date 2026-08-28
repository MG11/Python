class Solution:

    def findIsland(self, grid, r, c):
        if grid[r][c] == '0' or grid[r][c] == '#':
            return 0

        grid[r][c] = '#'

        directions = [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]

        for direction in directions:
            if 0 <= direction[0] < len(grid) and 0 <= direction[1] < len(grid[0]):
                self.findIsland(grid, direction[0], direction[1])
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        count = 0
        for r in range(row):
            for c in range(col):
                count += self.findIsland(grid, r, c)
        return count
        