"""
sort the array, take the median if odd length
take any value if first or second mid values if even length, then 
increase counter to match these values

https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/1217473/C%2B%2BPythonJava-2-Solutions-(w-and-wo-Median)-Explained-with-Example-implementation
"""
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            count += nums[j] - nums[i]
            j -= 1
            i += 1
        return count
