from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        major = nums[0]
        count = 1
        
        for i in nums[1:]:
            if(major == i):
                count += 1
            elif (count == 0):
                count = 1
                major = i
            else:
                count -= 1
        return major
        