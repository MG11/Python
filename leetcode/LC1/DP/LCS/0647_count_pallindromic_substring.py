# https://leetcode.com/problems/palindromic-substrings/discuss/105689/Java-solution-8-lines-extendPalindrome

class Solution:
    def expandcentre(self, s, i, j):
        stringFound = 0
        while(i >= 0 and j <len(s) and s[i] == s[j]):
            i -= 1
            j += 1
            stringFound += 1
        return stringFound
        
        
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            count += self.expandcentre(s, i, i)
            count += self.expandcentre(s, i, i+1)
        return count
        