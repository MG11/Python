from typing import List

class Solution:
    def getIndex(self, nums, target, lower):
        start = 0
        end = len(nums) - 1
        position = -1
        
        while(start <= end):
            mid = (start + end)//2
            if nums[mid] == target:
                position = mid
                # may be i can get this element at more smaller index
                if lower:
                    end = mid -1
                else:
                    start = mid +1
            elif nums[mid] < target:
                start = mid +1
            else:
                end = mid -1
        return position
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lowerIndex = self.getIndex(nums, target, True)
        if lowerIndex == -1:
            return [-1, -1]
        upperIndex = self.getIndex(nums, target, False)
        return [lowerIndex, upperIndex]
