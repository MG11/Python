class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        hashMap = {}
        maxlength = 0

        for i in range(len(s)):
            if s[i] not in hashMap or start > hashMap[s[i]]:
                hashMap[s[i]] = i
                end = i
            else:
                start = hashMap[s[i]] + 1
                hashMap[s[i]] = i
            maxlength = max(maxlength, end - start + 1)
        return maxlength

