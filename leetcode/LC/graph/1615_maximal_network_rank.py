"""
https://leetcode.com/problems/maximal-network-rank/discuss/1235181/C%2B%2B-O(N2)-and-O(N)-easy-to-understand
O(n^2) | O(n)    
"""

# take 1 1D vector to store road count, and one 2D vector to store connections

from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxrank = 0
        rank = [0 for i in range(n)]
        connections = set()
        
        for road in roads:
            connections.add((road[0], road[1]))
            rank[road[0]] += 1
            rank[road[1]] += 1
        
        for i in range(n):
            for j in range(i+1, n):
                currentrank = rank[i] + rank[j]
                if (i,j) in connections or (j, i) in connections:
                    currentrank -= 1
                maxrank = max(maxrank, currentrank)
        return maxrank
        