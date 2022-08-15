"""
TC: O(N*K + N*A) // N is max length str length, K is length of string
SC: O(N*K + N*A)

refer approach 2 of solutions
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for data in strs:
            chararray = [0]*26
            for d in data:
                chararray[ord(d) - 97] += 1
            key = '#'.join(map(str,chararray))
            ans[key].append(data)
        return list(ans.values())
    