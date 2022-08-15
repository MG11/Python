# TC: O(n*n*m)
#SC: O(n)
from typing import List

class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[-1] = True
        # end = len(s)
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i+len(w) <=len(s) and  w == s[i:i+len(w)]):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

# top down dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1): # O(n) n is length of string 
            for w in wordDict: # O(m) because m words
                if i >= len(w) and w == s[i-len(w):i]: # O(n)
                    dp[i] = dp[i-len(w)]
                if dp[i]:
                    break
        return dp[-1]
