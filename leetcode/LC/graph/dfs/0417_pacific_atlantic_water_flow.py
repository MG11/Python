"""
O(m*n) | O(m*n) [ for visit cells]

for first row and first col do dfs for pacific ocean
for last row and last col do dfs for atlantic ocean
in dfs check if the value at row, col can reach previous value, so, previous value is passed as parameter.
current value should not be greater than previous value, if it is then return else do dfs on adjacent value of that row, col
"""
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row = len(heights)
        col = len(heights[0])
        p = set()
        a = set()
        
        def dfs(r, c, visit, height):
            if (r,c) in visit or r < 0 or r >= row or c < 0 or c >= col or height > heights[r][c]:
                return
            visit.add((r,c))
            
            directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for d in directions:
                dfs(d[0], d[1], visit, heights[r][c])
        
        for c in range(col):
            dfs(0, c, p, heights[0][c])
            dfs(row-1, c, a, heights[row-1][c])
            
        
        for r in range(row):
            dfs(r,0, p, heights[r][0])
            dfs(r,col-1, a, heights[r][col-1])
        
        # do intersection of pacific and atlantic set
        ans = [v for v in p if v in a]
        return ans