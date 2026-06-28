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




# refer alex book
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        upperBound = self.findUpperlimit(nums, target)
        lowerBound = self.findLowerlimit(nums, target)
        return [lowerBound, upperBound]
    

    def findLowerlimit(self, nums, target):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1
    

    def findUpperlimit(self, nums, target):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid
        return right if nums[right] == target else -1
