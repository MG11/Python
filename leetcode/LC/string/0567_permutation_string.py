"""
https://leetcode.com/problems/permutation-in-string/discuss/102588/Java-Solution-Sliding-Window
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        
        l1 = [0]*26
        l2 = [0]*26 # always contains 0
        
        for x in s1:
            l1[ord(x) - ord('a')] += 1
        
        for i in range(len(s1)):
            l1[ord(s2[i]) - ord('a')] -= 1
        
        if l1 == l2:
            return True
        
        # i is end index
        for i in range(len(s1), len(s2)):
            print(s2[i])
            l1[ord(s2[i - len(s1)]) - ord('a') ] += 1
            l1[ord(s2[i]) - ord('a')] -= 1
            if l1 == l2:
                return True
        return False
