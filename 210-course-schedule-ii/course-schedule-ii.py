class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]


        for p in prerequisites:
            indegree[p[0]] += 1
            adj_list[p[1]].append(p[0])
        
        q = Deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while len(q):
            node = q.popleft()
            ans.append(node)
            for item in adj_list[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.append(item)
        return ans if len(ans) == numCourses else []