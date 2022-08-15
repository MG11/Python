from typing import List

class Solution:
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
        