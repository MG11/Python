class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevheight):
            if (r, c) in visit or r < 0 or c < 0 or r >= row or c >= col or heights[r][c] < prevheight:
                return False
            visit.add((r,c))

            directions = ((r-1, c), (r, c-1), (r, c+1), (r+1, c))

            for d in directions:
                dfs(d[0], d[1], visit, heights[r][c])
            


        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col-1])
        
        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row-1][c])
        
        ans = [list(v) for v in pac if v in atl]
        return ans

