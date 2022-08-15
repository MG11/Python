"""
traverse 1 array, put its value and count in set.
traverse 2nd array, check if it is in set and decrease set value
https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82243/Solution-to-3rd-follow-up-question
"""
from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        mapping = defaultdict(int)
        
        for num in nums1:
            mapping[num] += 1
        
        ans = []
        
        for num in nums2:
            if num in mapping and mapping[num] != 0:
                mapping[num] -= 1
                ans.append(num)
        return ans
