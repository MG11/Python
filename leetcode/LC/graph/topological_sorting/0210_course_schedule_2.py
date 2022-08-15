from collections import deque
from typing import List

"""
take an indegree array to store count of incoming nodes in a node.
take an adjacency list to store child of a node. ie. if 0--> 1 store [0] : [1, ]
take deque and store nodes whose indegree is 0
traverse while queue is not empty while printing the queue, also check adjacency list and degree indegree 
of adjacent nodes
"""

# O(n) | O(n)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adjacency_list = [ [] for _ in range(numCourses)]
        ans = []
        # p [1, 0] 0-->1
        for p in prerequisites:
            indegree[p[0]] += 1
            adjacency_list[p[1]].append(p[0])
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while(len(q)):
            c = q.popleft()
            ans.append(c)
            for a in adjacency_list[c]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)
        ans = ans if len(ans) == numCourses else []
        return ans
        