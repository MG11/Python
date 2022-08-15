from typing import List

class Solution:
    def twoSum(self, nums, i, ans):
        start = i+1
        end = len(nums) - 1
        while(start < end):
            currentSum = nums[start] + nums[end] + nums[i]
            if currentSum == 0:
                ans.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
                # shift end to avoid same start and end values
                while(start < end and nums[end] == nums[end+1]):
                    end -= 1
            elif currentSum > 0:
                end -= 1
            else:
                start += 1

        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort used O(n) space, O(nlogn) time
        nums.sort() 
        ans = []
        for i in range(len(nums)):
            # pick first, if there are duplicates. so, that second one can be used
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, ans)
        return ans
        