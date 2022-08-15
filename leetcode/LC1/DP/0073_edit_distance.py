# https://www.youtube.com/watch?v=WgmZ-5qAHJ8
# O(mn) | O(mn) 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        
        # w2 is col and w1 is row, refer copy for exact dp table  and approach
        dp = [[i+j for i in range(w2+1)] for j in range(w1+1)]
        for i in range(1, w1+1):
            for j in range(1, w2+1):
                x = 1
                if(word1[i-1]  == word2[j-1]):
                    x = 0
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + x)
        return dp[w1][w2]


# https://leetcode.com/problems/delete-operation-for-two-strings/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        
        # w2 is col and w1 is row, refer copy for exact dp table  and approach
        dp = [[i+j for i in range(w2+1)] for j in range(w1+1)]
        for i in range(1, w1+1):
            for j in range(1, w2+1):
                # in case the alphabets are not same then delete both so count 2 is taken
                x = 2
                if(word1[i-1]  == word2[j-1]):
                    x = 0
                # minimum of delete from first, delete from second or delete from both
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + x)
        return dp[w1][w2]
        