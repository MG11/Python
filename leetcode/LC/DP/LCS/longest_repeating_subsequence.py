# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1

#https://www.youtube.com/watch?v=hbTaCmQGqLg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29

class Solution:
    	def LongestRepeatingSubsequence(self, str):
		# Code here
            n = len(str)
            # first bracket is for col and last is for row
            dp = [[0 for i in range(n+1)] for j in range(n+1)]
    #         to find LPS, do LCS on s and reverse of s
            s1 = str[:]
            for i in range(1, n+1): #row
                for j in range(1, n+1): #col
                    if(str[i-1] == s1[j-1] and i != j):
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[n][n]
