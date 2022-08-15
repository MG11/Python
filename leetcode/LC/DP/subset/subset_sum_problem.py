
# recusrion
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        if(sum == 0):
            return True
        if(N == 0):
            return False
        if(arr[N-1] > sum):
            return self.isSubsetSum(N-1, arr, sum)
        return self.isSubsetSum(N-1, arr, sum - arr[N-1]) or self.isSubsetSum(N-1, arr, sum)

# DP
class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp = [[False for i in range(sum+1)] for j in range(N+1)]
        # set 1 when sum is 0
        for i in range(N+1):
            dp[i][0] = True
        
        for i in range(1, N+1):
            for j in range(1, sum+1):
                if(arr[i-1] <= j):
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][sum]
