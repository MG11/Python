from typing import List

class Solution1:
    def rob(self, nums: List[int]) -> int:
        robnextplusone = 0
        n = len(nums)
        robnext = nums[n -1]
        current = robnext
        
        for i in range(n-2, -1, -1):
            current = max(nums[i] + robnextplusone, robnext)
            robnextplusone = robnext
            robnext = current
        return current

    
# recusrion : TLE for big test cases
class Solution2:
    def robHelper(self, nums, index):
        if index < 0:
            return 0
        return max(nums[index] + self.robHelper(nums, index-2), self.robHelper(nums, index-1))
        
    def rob(self, nums: List[int]) -> int:
        return self.robHelper(nums, len(nums) -1)

    
# recusion with memorization
class Solution3:
    def __init__(self):
        self.memo = []
        
    def robHelper(self, nums, length):
        if(length < 0):
            return 0
        if(self.memo[length] != -1):
            return self.memo[length]
    
        self.memo[length] = max(nums[length-1] + self.robHelper(nums, length-2), self.robHelper(nums, length-1))
        return self.memo[length]
        
    def rob(self, nums: List[int]) -> int:
        self.memo = [-1 for i in range(len(nums) +1)]
        self.memo[0] = 0
        return self.robHelper(nums, len(nums))
    
# 1D DP
class Solution4:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1 for i in range(n +2)]
        memo[0] = 0
        memo[1] = 0
        
        for i in range(2,n+2):
            memo[i] = max(nums[i-2]+memo[i-2], memo[i-1])
        return memo[-1]

# 1 DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        secondLast = 0
        Last = 0
        
        for i in range(2,n+2):
            current = max(nums[i-2] + secondLast, Last)
            secondLast = Last
            Last = current
        return current
    

#  https://leetcode.com/problems/house-robber-ii/
class Solution:
    def robHelper(self, nums, start, end):
        secondLast, Last,current = 0, 0, 0
        for i in range(start, end):
            current = max(nums[i] + secondLast, Last)
            secondLast = Last
            Last = current
        return current
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(len(nums) == 1):
            return nums[0]
        return max(self.robHelper(nums, 0, n-1), self.robHelper(nums, 1,n))
        