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
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
    