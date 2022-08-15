from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        fresh_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        if fresh_oranges == 0:
            return 0
        
        count = 0
        while(len(queue)):
            count += 1
            size = len(queue)
            for o in range(size):
                i, j = queue.popleft()
                directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for d in directions:
                    if 0 <= d[0] < len(grid) and 0 <= d[1] < len(grid[0]) and grid[d[0]][d[1]] == 1:
                        grid[d[0]][d[1]] = 2
                        queue.append((d[0], d[1]))
                        fresh_oranges -= 1
        return count -1 if not fresh_oranges else -1
                    