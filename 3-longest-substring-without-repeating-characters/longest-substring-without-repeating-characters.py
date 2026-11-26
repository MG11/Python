class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start, end = 0, 0
        charMap = {}

        while end < len(s):
            if s[end] in charMap and charMap[s[end]] >= start:
                maxLength = max(maxLength, end - start)
                start = charMap[s[end]] + 1
            charMap[s[end]] = end
            end += 1
        return max(maxLength, end - start)
        