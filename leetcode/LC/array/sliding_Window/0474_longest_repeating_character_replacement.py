# https://www.youtube.com/watch?v=gqXU1UyA8pk

# O(n) | O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left = 0
        res = 0
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1
            if r - left + 1 - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)
        return res


# refer neetcode video: https://www.youtube.com/watch?v=gqXU1UyA8pk
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxf = 0
        l, r = 0, 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])
            if r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
