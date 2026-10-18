class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False]*col for _ in range(row)]
        def dfs(r,c):
            nonlocal visited
            visited[r][c] = True
            if grid[r][c] != '1':
                return 0

            directions = [(r - 1, c), (r , c - 1), (r + 1, c), (r, c + 1)]

            for d in directions:
                if 0 <= d[0] < row and 0 <= d[1] < col and not visited[d[0]][d[1]]:
                    dfs(d[0], d[1])
    
            return 1

        count = 0
        for r in range(row):
            for c in range(col):
                if(grid[r][c] == '1' and not visited[r][c] and dfs(r,c)):
                    count += 1
        return count
        
