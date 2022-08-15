from typing import List

#  TC: O(number of strings* length of smallest string)
# SC: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = []
#          for each character traverse in all string if the character is found in all strings  
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if(len(strs[j]) <= i or strs[j][i] != strs[0][i]):
                    return ''.join(output)
            output.append(strs[0][i])
        return ''.join(output)
        