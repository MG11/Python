from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap: # 'in' in dict is O(1) 
                return [i, hashmap[target-nums[i]]]
            else:
                hashmap[nums[i]] = i
        return [-1, -1]
                