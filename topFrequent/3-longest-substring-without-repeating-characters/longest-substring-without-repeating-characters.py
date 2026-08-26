class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0
        charMap = {}

        for end in range(len(s)):
            if s[end] in charMap and charMap[s[end]] >= start:
                start = charMap[s[end]] + 1
            charMap[s[end]] = end
            maxLength = max(maxLength, end - start + 1)
        return maxLength
