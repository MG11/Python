
# refer alex book for solution.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        currentfrq = [0]*26
        askedfrq = [0]*26

        for c in p:
            askedfrq[ord(c) - ord('a')] += 1

        start = 0
        end = 0
        indics = []

        while end < len(s):
            currentfrq[ord(s[end]) - ord('a')] += 1
            end += 1

            if end - start >= len(p):
                if(self.checkfrequencyMatch(currentfrq, askedfrq)):
                    indics.append(start)
                currentfrq[ord(s[start]) - ord('a')] -= 1
                start += 1
        return indics

    def checkfrequencyMatch(self, currentfrq, askedfrq):
        for i in range(26):
            if currentfrq[i] != askedfrq[i]:
                return False
        return True

