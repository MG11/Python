from typing import str
class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = []
        for word in strs:
            ans.append(str(len(word)))
            ans.append('#')
            ans.append(word)
        return ''.join(ans)
        

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        i = 0
        ans = []
        while i < len(s):
            count = ''
            result = []
            while  i < len(s) and s[i] != '#':
                count += s[i]
                i += 1
            count = int(count)
            for j in range(i+1, count+i+1):
                result.append(s[j])
            result.append('')
            i = count+i+1
            ans.append(''.join(result))
        return ans
                
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))