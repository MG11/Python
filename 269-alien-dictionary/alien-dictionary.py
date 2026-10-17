class Solution:
    def alienOrder(self, words: list[str]) -> str:
        indegree = {c: 0 for word in words for c in word}

        adj_list = defaultdict(list)

        for first, second in zip(words, words[1:]):
            for c, d in zip(first, second):
                if c != d:
                    indegree[d] += 1
                    adj_list[c].append(d)
                    break
            else:
                if len(first) > len(second):
                    return ""
        
        print(adj_list)
        q = deque()

        for key, val in indegree.items():
            if not val:
                q.append(key)
        
        ans = []
        while len(q):
            l = len(q)

            for i in range(l):
                e = q.popleft()
                ans.append(e)
                for a in adj_list[e]:
                    indegree[a] -= 1
                    if indegree[a] == 0:
                        q.append(a)
        return "".join(ans) if len(ans) == len(indegree) else ""
