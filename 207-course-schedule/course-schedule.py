class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]


        for p in prerequisites:
            indegree[p[0]] += 1
            adj_list[p[1]].append(p[0])
        
        q = Deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while len(q):
            node = q.popleft()
            count += 1
            for item in adj_list[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.append(item)
        return count == numCourses
