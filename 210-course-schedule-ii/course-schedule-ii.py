class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # [0 , 1]   1 --> 0, indegree 0 is 1, adj 1 is [0]

        indegree = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]

        for p in prerequisites:
            indegree[p[0]] += 1
            adj_list[p[1]].append(p[0])
        
        q = Deque()
        for i in range(numCourses):
            q.append(i) if indegree[i] == 0 else None
        
        output = []
        while len(q):
            item = q.popleft()
            output.append(item)

            for node in adj_list[item]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        return output if len(output) == numCourses else []
