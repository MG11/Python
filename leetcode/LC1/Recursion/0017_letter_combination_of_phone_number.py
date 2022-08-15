from typing import List

class Solution:
    my_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    def __init__(self):
        self.ans = []
        
    def letter_helper(self, digits, index, output):
        if len(digits) == index:
            self.ans.append("".join(output)) if output else None
            output = []
            return
        
        for k in self.my_map[digits[index]]:
            output.append(k)
            self.letter_helper(digits, index+1, output)
            # pop k so that it is not appended in next iteration
            output.pop()
        return
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.letter_helper(digits, 0, [])
        return self.ans
        