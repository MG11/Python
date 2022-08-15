from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        r = len(grid2)
        c = len(grid2[0])
        def dfs(row, col):
            res = 1
            grid2[row][col] = 0
            directions = [(row -1, col), (row+1, col), (row, col-1), (row, col+1)]
            for d in directions:
                if 0 <= d[0] < r and 0 <= d[1] < c and grid2[d[0]][d[1]]:
                    # both sides are evaluated in & (bitwise)
                    res = res & dfs(d[0], d[1])
            return res and grid1[row][col]
            
        for row in range(r):
            for col in range(c):
                if grid2[row][col]:
                    count += dfs(row, col)
        return count
