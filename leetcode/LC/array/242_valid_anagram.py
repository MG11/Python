class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = {}

        for n in s:
            hashMap[n] = hashMap.get(n, 0) + 1
        
        for n in t:
            hashMap[n] = hashMap.get(n,0) - 1
            if hashMap[n] == 0:
                del hashMap[n]

        if hashMap == {}:
            return True
        return False
