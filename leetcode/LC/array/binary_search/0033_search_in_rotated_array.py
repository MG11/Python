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
