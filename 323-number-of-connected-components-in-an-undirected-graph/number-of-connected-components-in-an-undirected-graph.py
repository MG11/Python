class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = {i:i for i in range(n)}

        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        connect = n
        for edge in edges:
            rootA = find(edge[0])
            rootB = find(edge[1])

            if rootA != rootB:
                parent[rootB] = rootA
                connect -= 1
                
        return connect
