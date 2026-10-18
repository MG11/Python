
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


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution1:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        map = {}

        q = deque()
        q.append(node)

        while len(q):
            n = q.popleft()
            newnode = map.get(n, Node(n.val))
            map[n] = newnode
            for a in n.neighbors:
                neighbor = map.get(a)
                if not neighbor:
                    neighbor = Node(a.val)
                    map[a] = neighbor
                    q.append(a)
                newnode.neighbors.append(neighbor)
        return map.get(node)
    
