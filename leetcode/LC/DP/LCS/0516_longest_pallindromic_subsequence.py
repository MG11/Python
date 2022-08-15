class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # first bracket is for col and last is for row
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
#         to find LPS, do LCS on s and reverse of s
        s1 = s[::-1]
        for i in range(1, n+1): #row
            for j in range(1, n+1): #col
                if(s[i-1] == s1[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][n]
        

# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# https://www.youtube.com/watch?v=CFwCCNbRuLY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=27


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # first bracket is for col and last is for row
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
#         to find LPS, do LCS on s and reverse of s
        s1 = s[::-1]
        for i in range(1, n+1): #row
            for j in range(1, n+1): #col
                if(s[i-1] == s1[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # in case of minium number of insertion or deletion return length of string - pallindrome length
        return len(s) - dp[n][n]
