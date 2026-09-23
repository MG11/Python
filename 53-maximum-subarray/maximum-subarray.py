class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for n in nums:
            currentSum += n
            maxSum = max(maxSum, currentSum)

            if (currentSum < 0):
                currentSum = 0
        return maxSum