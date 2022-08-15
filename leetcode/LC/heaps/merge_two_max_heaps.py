"""
heapify: O(n):
approach: mentioned in copy
"""

class Solution():
    def percolatedown(self, ans, i):
        if i > len(ans):
            return
        if (2*i+2 < len(ans)):
            idx = 2*i+2 if ans[2*i+2] > ans[2*i+1] else 2*i+1
        elif (2*i+1 < len(ans)):
            idx = 2*i+1
        else:
            return
        if(ans[i] < ans[idx]):
            ans[i], ans[idx] = ans[idx], ans[i]
            self.percolatedown(ans, idx)
        return
        
    def mergeHeaps(self, a, b, n, m):
        #your code here
        ans = a[:]
        ans.extend(b)
        for i in range(len(ans)//2 -1, -1, -1):
            self.percolatedown(ans, i)
        return ans
