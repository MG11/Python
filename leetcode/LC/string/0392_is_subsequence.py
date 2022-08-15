class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ss = 0
        st = 0
        
        while(st < len(t) and ss < len(s)):
            if t[st] == s[ss]:
                st += 1
                ss += 1
            else:
                st += 1
        if (ss == len(s)):
            return True
        return False
        