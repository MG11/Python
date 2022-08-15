from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) -1
        mid = 0
        # here search size is less than or equal to 3 always
        while start + 1 < end:
            mid = (start + end)//2
            if(nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]):
                return mid
            elif(nums[mid+1] > nums[mid]):
                start = mid+1
            else:
                end = mid - 1
        # for the case when search size is 2 or 1
        return start if nums[start] >= nums[end] else end
