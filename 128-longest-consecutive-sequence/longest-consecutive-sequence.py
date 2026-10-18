class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        data = set(nums)

        maxlen = 0
        for n in data:
            if n - 1 in data:
                continue
            count = 1
            x = n
            while x + 1 in data:
                count += 1
                x += 1
            maxlen = max(maxlen, count)
        return maxlen
 