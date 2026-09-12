class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxValue = nums[0]
        curr_min, curr_max = 1, 1

        for n in nums:
            values = (n, curr_min*n, curr_max*n)
            curr_min = min(values)
            curr_max = max(values)
            maxValue = max(maxValue, curr_max)
        return maxValue

            