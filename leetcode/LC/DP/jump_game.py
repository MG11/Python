from typing import List

# https://leetcode.com/problems/jump-game-ii/
"""
take left and right pointers, these are the ranges i can land from previous point.
now, from these range find farthest point in can reach that will be my right and left will be right +1
"""
# greedy O(n) | O(1)
class Solution:
    def jump1(self, nums: List[int]) -> int:
        left, right, count = 0, 0, 0
        
        while(right < len(nums) -1):
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, nums[i] + i)
            left = right + 1
            right = farthest
            print(left, right)
            count += 1
        return count

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf') for i in range(len(nums))]
        dp[0] = 0
        
        for i in range(1, len(nums)):
            for j in range(i):
                if(nums[j] + j >= i):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left, right, farthest = 0, 0, 0
        
        # if left becomes more than right, it can't reach at the last
        while(left <= right):
            for i in range(left, right+1):
                if(right >= len(nums)-1): 
                    return True # if right is more than last index, it can reach end
                if(right >= len(nums) - 1): return True
                farthest = max(farthest, nums[i] + i)
            left = right + 1
            right = farthest
        return False


# https://leetcode.com/problems/jump-game-iii/
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if(start < 0 or start >= len(arr) or arr[start] < 0):
            return False
        arr[start] = arr[start]*-1
        if(arr[start] == 0):
            return True
        return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        