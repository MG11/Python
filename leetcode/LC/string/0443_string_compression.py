from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            j = i + 1
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            chars[res] = chars[i]
            res += 1
            count = j - i
            if count > 1:
                for ch in str(count):
                    chars[res] = ch
                    res += 1
            i = j
        return res
