# O(n+e) | O(v)
from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = [0]*n
        q = deque([start])
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        visited[start] = 1
        
        while(len(q)):
            v = q.popleft()
            if v == end:
                return True
            for i in adj_list[v]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
        return False        
        