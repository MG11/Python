# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        data = {0:1} # key stores sum, value stores number of times this sum occured
        counter = 0
        sum = 0
        for i in nums:
            sum += i
            if data.get(sum - k):
                counter += data[sum-k]
            if not data.get(sum):
                data[sum] = 1
            else:
                data[sum] += 1
        return counter
