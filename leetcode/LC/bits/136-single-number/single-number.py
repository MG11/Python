class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = nums[0]
        for i in range(1, len(nums)):
            output = start^nums[i]
            start = output
        return start
