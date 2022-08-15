# O(n) | O(1)
"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/927654/C%2B%2BJavaPython3-Simple-time-O(n)-space-O(1)-a-small-array-is-all-you-need
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0]*26
        
        for a in s:
            freq[ord(a) - ord('a')] += 1
        
        freq.sort(reverse=True)
        
        maxallowed = freq[0]
        count = 0
        for f in freq:
            if not f:
                break
            if f > maxallowed:
                count += f - maxallowed
                if maxallowed != 0: maxallowed -= 1
            else:
                maxallowed = f - 1
           
        return count
