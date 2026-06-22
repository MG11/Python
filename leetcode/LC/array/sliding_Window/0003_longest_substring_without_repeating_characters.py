class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        maxLength = 0
        data = {}

        while end < len(s):
            if s[end] in data and data[s[end]] >= start:
                maxLength = max(end - start, maxLength)
                start = data[s[end]] + 1
            data[s[end]] = end
            end += 1
        return max(end - start, maxLength)
