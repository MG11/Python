class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        n = len(word)
        ans = 0

        for i in range(n):
            seen = {}
            for j in range(i, n):
                ch = word[j]
                if ch not in vowels:
                    break
                seen[ch] = seen.get(ch, 0) + 1
                if len(seen) == 5:
                    ans += 1
        return ans
