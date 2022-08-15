"""
Check whether or not there are n - 1 edges. If there's not, then return false.
Check whether or not the graph is fully connected. Return true if it is, false if otherwise.
https://leetcode.com/problems/graph-valid-tree/solution/
https://leetcode.com/problems/graph-valid-tree/discuss/69019/Simple-and-clean-c%2B%2B-solution-with-detailed-explanation.
"""
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if number of edges are less or more than n-1, it cannot be tree
        if len(edges) != n-1:
            return False
        
        values = []
        for i in range(n):
            values.append(i)
        
        for i in range(n-1):
            s = edges[i][0] #parent
            f = edges[i][1] #child
            while(values[s] != s): s = values[s]
            while(values[f] != f): f = values[f]
            if(values[s] == values[f]): #if they have same parent that means cycle is found, it cannot be tree
                return False
            # store parent in child node
            values[f] = s
        return True
