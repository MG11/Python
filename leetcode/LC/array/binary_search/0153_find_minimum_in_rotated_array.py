 #  Number of Times a Sorted array is Rotated is the index of the minium element

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        n = len(nums)
        
        while(start < end):
            mid = (start + end)//2
            
            if nums[mid] > nums[end]:
                start = mid +1
            else:
                end = mid
        return nums[start]

    def findMin2(self, nums: List[int]) ->int:
        start = 0
        end = len(nums) - 1
        mid = 0
        n = len(nums)

        while(start < end):
            mid = (start + end)//2
            prev = (mid - 1 + n)%n
            # only minimum element is less than its previous in sorted rotated array
            # ex: 6 7 1 2 3 4 5 
            if(nums[mid] < nums[prev]):
                return nums[mid]
            # if the mid one is less than start then discard right part 
            # else minimum will always be at unsorted subpart
            if(nums[mid] < nums[start]):
               end = mid -1
            else:
                start = mid + 1
        return nums[start] if nums[start] <= nums[end] else nums[end]
