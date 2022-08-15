# recursion with memorization
# O(n) | O(n)
class Solution1:
    def __init__(self):
        self.memo = {} # key is index value is ans at that index
        
    def numDecodingsHelper(self, index, s):
        if(index == len(s)):
            return 1
        if(s[index] == '0'):
            return 0
        if(index == len(s) - 1):
            return 1
        if(self.memo.get(index)):
            return self.memo[index]
        
        ans = self.numDecodingsHelper(index + 1, s)
        if(int(s[index: index + 2]) <= 26):
            ans += self.numDecodingsHelper(index + 2, s)
        self.memo[index] = ans
        return ans
        
        
    def numDecodings(self, s: str) -> int:
        return self.numDecodingsHelper(0, s)

# DP
class Solution:
    def numDecodings(self, s: str) -> int:
        if not len(s):
            return 0
        if(s[0] == '0'):
            return 0
        if len(s) == 1:
            return 1
        dp = [0 for i in range(len(s))]
        # initialize last and second last values with the conditions
        dp[-1] = 1 if s[-1] != '0' else 0
        dp[-2] = 0 if s[-2] == '0' else dp[-1] if int(s[-2:]) > 26 else dp[-1] + 1
        for i in range(len(s) - 3,-1, -1):
            if(s[i] == '0'):
                dp[i] = 0
            elif(int(s[i:i+2]) > 26):
                dp[i] = dp[i+1]
            else:
                dp[i] = dp[i+1] + dp[i+2]
        return dp[0]
    