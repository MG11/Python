from collections import deque, defaultdict
from typing import List

# O(C) | O(E) # C is sum of all alphabets of words
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(list)
        
        # set indegree to 0 for every alphabet
        indegree = {c:0 for word in words for c in word}
        
        # create adjacency list
        for first, second in zip(words, words[1:]):
            for c, d in zip(first, second):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].append(d)
                        indegree[d] += 1
                    break
            else:
                # ex : in case ape, ap
                if len(first) > len(second): return ""
        
        q = deque()
        
        # add in q with 0 indegree
        for key, value in indegree.items():
            if value == 0:
                q.append(key)
        
        # topological sort
        ans = []
        while(len(q)):
            a = q.popleft()
            ans.append(a)
            for adj in adj_list[a]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
        
        # if all words are not covered return ''
        return ''.join(ans) if len(ans) == len(indegree) else ""
        