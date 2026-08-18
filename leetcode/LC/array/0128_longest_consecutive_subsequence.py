class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0
        for num in nums:
            if (num - 1) in nums:
                continue
            start = num
            size = 0
            while start in nums:
                size += 1
                start += 1
            longest = max(longest, size)
        return longest
