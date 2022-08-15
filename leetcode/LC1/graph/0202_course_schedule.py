"""
do topological sort and check if cycle is found
"""
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjacency_list = [ [] for _ in range(numCourses)]
        
        # p [1, 0] 0-->1
        for p in prerequisites:
            indegree[p[0]] += 1
            adjacency_list[p[1]].append(p[0])
        q = deque()
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while(len(q)):
            c = q.popleft()
            count += 1
            for a in adjacency_list[c]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)
        return count == numCourses
    