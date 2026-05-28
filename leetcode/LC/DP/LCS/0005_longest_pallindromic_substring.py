# refer bytebyego pattern book for solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        startIndex = 0
        maxLength = 0

        dp = [[False]*len(s) for _ in range(len(s))]

        length = len(s)
        for i in range(length):
            dp[i][i] = True
            startIndex = i
            maxLength = 1
        
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                startIndex = i
                maxLength = 2

        for substring in range(3, length + 1):
            for i in range(length - substring + 1):
                j = i + substring - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and j - i + 1 > maxLength:
                    startIndex = i
                    maxLength = j - i + 1
        return s[startIndex : startIndex + maxLength]
