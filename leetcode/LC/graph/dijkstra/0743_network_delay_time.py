from typing import List
from collections import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        1. create adjacency matrix
        2. initialize min heap
        3. create distance to store final weight at that index node, initialize it with infinity
        """
        # create adjacency list with initial node as graph index and values as vector of pairs with values target node and weight.
        adj_list = [{} for _ in range(n+1)]
        
        for u,v, w in times:
            adj_list[u][v] = w
        
        minheap = [(0, k)]
        distance = [float('inf') for _ in range(n+1)]
        
        # 0 is taken extra for indexing purpose
        distance[0] = 0
        
        # distance of source is 0
        distance[k] = 0
        
        while minheap:
            wt, n = heapq.heappop(minheap)
            for target, weight in adj_list[n].items():
                if distance[target] > wt + weight:
                    heapq.heappush(minheap, (wt+weight, target))
                    distance[target] = wt + weight
        if max(distance) == float('inf'): return -1
        return max(distance)
        