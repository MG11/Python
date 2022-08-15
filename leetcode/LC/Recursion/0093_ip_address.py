# O(27) | O(4)
from typing import List

class Solution:
    def __init__(self):
        self.res = []
    
    def helper(self, s, index, output):
        if index == len(s) and len(output) == 4:
            self.res.append('.'.join(output))
            return
        if len(output) == 4 or index == len(s):
            return 
        
        i = index
        if s[i] != '0' and i + 3 <= len(s) and int(s[i:i+3]) <=255:
            output.append(s[i:i+3])
            self.helper(s, i+3, output)
            output.pop()

        if s[i] != '0' and i+2 <= len(s):
            output.append(s[i:i+2])
            self.helper(s, i+2, output)
            output.pop()


        output.append(s[i])
        self.helper(s, i+1, output)
        output.pop()
            
            
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.helper(s, 0, [])
        return self.res
