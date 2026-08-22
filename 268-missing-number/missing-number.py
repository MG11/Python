class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)

        for i in range(len(nums)):
            ans ^= i^nums[i]
        return ans

"""
take xor of the list: [0, 1, 2, 3]
and xor of input list: [0, 1, 3] (input array)

return will the ans which is extra in first list and missing in second list
"""