class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = {i:i for i in range(n)}

        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        
        for edge in edges:
            rootA = find(edge[0])
            rootB = find(edge[1])

            if rootA != rootB:
                parent[rootB] = rootA
        
        count = 0
        for key, value in parent.items():
            if key == value:
                count += 1
        return count
