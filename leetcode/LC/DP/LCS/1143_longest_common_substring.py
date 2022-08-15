#https://www.youtube.com/watch?v=sSno9rV8Rhg
# https://www.youtube.com/watch?v=hR3s9rGlMTU&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=21

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # first bracket is for col and last is for row
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
    
    
        for i in range(1, n+1): #row
            for j in range(1, m+1): #col
                if(text1[i-1] == text2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]


# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1/#
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        n = len(S1)
        m = len(S2)
        # first bracket is for col and last is for row
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
    
        maximum = 0
        for i in range(1, n+1): #row
            for j in range(1, m+1): #col
                if(S1[i-1] == S2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maximum = max(maximum, dp[i][j])
                else:
                    # chain broke
                    dp[i][j] = 0
        return maximum

# https://leetcode.com/problems/shortest-common-supersequence/

# m + n - lcs

# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1

#  find lcs delete : len(y) - lcs insert: len(x) - lcs
