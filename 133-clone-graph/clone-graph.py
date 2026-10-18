"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
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
    




