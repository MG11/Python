from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            mid = (low + high)//2
            if (nums[mid] == target):
                return mid
            # if nums[low] is less than nums[mid] then left part is sorted
            if (nums[low] <= nums[mid]):
                # if target is in sorted part 
                if(nums[low] <= target and nums[mid] > target):
                    high = mid - 1
                # if target is in unsorted part
                else:
                    low = mid + 1
            # else right part is sorted
            else:
                if(nums[high] >= target and nums[mid] < target):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1



# https://www.youtube.com/watch?v=5qGrJbHhqFs

# first find which part is sorted.. then checkif target is present in sorted part.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[start]:  # second half sorted
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else: # first half sorted
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
