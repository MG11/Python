# O(n) | O(charsetlength)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        curentLength  = 0
        hashmap = {} # key: character, value : index
        
        start, end = 0, 0
        
        for i in range(len(s)):
            if(hashmap.get(s[i], None) != None and hashmap.get(s[i]) >= start):
                start = hashmap[s[i]] + 1
                curentLength = i - start + 1
            else:
                curentLength += 1
            hashmap[s[i]] = i
            maxLength = max(maxLength, curentLength)
        return maxLength
        