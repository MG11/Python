class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if n != len(edges) + 1:
            return False
        parent = {k:k for k in range(n)}

        def find(n):
            while(parent[n] != n):
                n = parent[n]
            return n
        
        for edge in edges:
            rootA = find(edge[0])
            rootB = find(edge[1])
            if rootA == rootB:
                return False
            parent[rootB] = rootA

        return True
        