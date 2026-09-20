class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCharFreq = 0
        letters = [0]*26

        start, end = 0, 0

        while end < len(s):
            position = ord(s[end]) - 65
            letters[position] += 1
            maxCharFreq = max(maxCharFreq, letters[position])
            if (end - start + 1 - maxCharFreq > k):
                letters[ord(s[start]) - 65] -= 1
                start += 1
            end += 1
        return end - start
