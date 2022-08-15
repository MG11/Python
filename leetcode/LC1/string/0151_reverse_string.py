"""
trim white spaces and store it in array
reverse whole string
reverse each word
"""
class Solution:
    def convert_to_array(self, s):
        s = s.strip()
        output = []
        for i in range(0, len(s)):
            if i > 0 and s[i] == s[i-1] == ' ':
                continue
            output.append(s[i])
        return output
    
    def reverse(self, l, start, end):
        while(start < end):
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1
    
    def reverse_words(self, l):
        start = 0
        for i in range(0, len(l) - 1):
            if(l[i] == ' '):
                self.reverse(l, start, i -1)
                start = i+1
        self.reverse(l,start, len(l) - 1)
        
    def reverseWords(self, s: str) -> str:
        l = self.convert_to_array(s)
        self.reverse(l, 0, len(l) - 1)
        self.reverse_words(l)
        return ''.join(l)
