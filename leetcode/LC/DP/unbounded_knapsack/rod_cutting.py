# https://practice.geeksforgeeks.org/problems/rod-cutting0840/1#

#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        p = len(price)
        dp = [[0 for i in range(n+1)] for j in range(p+1)]
        # print(dp)
        # base cases
        # first row and first columns to be zero

        # set price ranges
        wt = [i+1 for i in range(len(price))]
        for i in range(1, p+1):
            for j in range(1, n+1):
                if(wt[i-1]<= j):
                    dp[i][j] = max(price[i-1] + dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        #print(dp)
        return dp[n][p]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends