class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            if grid[r][c] != '1':
                return 0
            
            grid[r][c] = '#'

            directions = [(r - 1, c), (r , c - 1), (r + 1, c), (r, c + 1)]

            for d in directions:
                if (0 <= d[0] < row and 0 <= d[1] < col):
                    dfs(d[0], d[1])
    
            return 1

        count = 0
        for r in range(row):
            for c in range(col):
                if(grid[r][c] == '1' and dfs(r,c)):
                    count += 1
        return count
        
