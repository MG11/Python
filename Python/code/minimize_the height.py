# https://www.youtube.com/watch?v=Av7vSnPSCtw

# User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        big = 0
        small = 0
        ans = arr[-1] - arr[0]

        for i in range(1, n):
            big = max(arr[-1] - k, arr[i - 1] + k)
            small = min(arr[0] + k, arr[i] - k)
            if small > 0:
                ans = min(ans, (big - small))

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends