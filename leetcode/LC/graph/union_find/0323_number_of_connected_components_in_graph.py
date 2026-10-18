class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        # to find the root node
        def find(res):
            while par[res] != res:
                res = par[res]
            return res
        
        # to add paths
        def union(p1, p2):
            p1, p2 = find(p1), find(p2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                rank[p2] += rank[p1]
                par[p1] = p2
            else:
                rank[p1] += rank[p2]
                par[p2] = p1
            return 1


# do dfs of for each node (like number of island)
class Solution1:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjlist = defaultdict(list)
        for edge in edges:
            adjlist[edge[0]].append(edge[1])
            adjlist[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for adj in adjlist[node]:
                if adj not in visited:
                    dfs(adj)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count

        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res



# union find (latest))
class Solution2:
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

