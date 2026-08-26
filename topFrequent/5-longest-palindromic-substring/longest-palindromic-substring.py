class Solution:
    def longestPalindrome(self, s: str) -> str:
        outputString = ""
        maxLength = 0

        for i in range(len(s)):

            # odd length
            start = i
            end = i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            if end - start - 1 > maxLength:
                maxLength = end - start - 1
                outputString = s[start + 1: end]
            
            # even length

            start = i
            end = i + 1

            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            if end - start - 1 > maxLength:
                maxLength = end - start - 1
                outputString = s[start + 1: end]
        
        return outputString


"""
neetcode
for each index, 
check for even and odd length separately. 

now: check if index - and index + 1 are same, if same check more else, calculate 
length and output string
"""