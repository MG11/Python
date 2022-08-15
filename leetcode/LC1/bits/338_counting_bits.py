# check approach 2 in solution
"""
TC: O(n) SC: O(1)
https://leetcode.com/problems/counting-bits/
"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = 1
        diff = 1
        ans = [0]
        for i in range(1,n+1):
            ans.append(ans[i - diff] + 1)
            counter -= 1
            if counter == 0:
                counter = diff*2
                diff = counter
        return ans
