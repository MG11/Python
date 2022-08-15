"""
https://leetcode.com/problems/longest-consecutive-sequence/solution/
approach 3
O(n) | O(n)
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0
        numset = set(nums)
        
        # set is iterable, it is O(n) as inner while loop is executed only once.
        for num in numset:
            if num -1 not in numset:
                currentLength = 1
                while num + currentLength in numset:
                    currentLength += 1
                longestSequence = max(currentLength, longestSequence)
        return longestSequence

        