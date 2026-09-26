class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        data = {'a', 'e', 'i', 'o', 'u'}
        last_seen = {}
        total = 0
        left, right = 0, 0
        map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        while right < len(word):
            if word[right] in data:
                last_seen[word[right]] = right
                if len(last_seen) == 5:
                    min_pos = min(last_seen.values())
                    total += min_pos - left + 1
            else:
                last_seen.clear()
                left = right + 1
            right += 1
        return total
