class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxValue = nums[0]
        currMin, currMax = 1, 1

        for n in nums:
            values = (n, currMin*n, currMax*n)
            currMin = min(values)
            currMax = max(values)
            maxValue = max(maxValue, currMax)
        return maxValue
