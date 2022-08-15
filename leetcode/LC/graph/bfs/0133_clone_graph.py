
# Definition for a Node.
"""
push first node in queue, 
clone it in a map if already not there, push its neighbour in queue if already not cloned.
set neighbours
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {node: Node(node.val)}
        q = deque([node])
        while(len(q)):
            n = q.popleft()
            for neighbour in n.neighbors:
                if not visited.get(neighbour, None):
                    visited[neighbour] = Node(neighbour.val)
                    q.append(neighbour)
                visited[n].neighbors.append(visited[neighbour])      
        return visited[node]