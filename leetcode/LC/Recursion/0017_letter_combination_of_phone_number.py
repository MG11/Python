# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/1148252/Short-and-Easy-Solutions-or-Multiple-Approaches-Explained-or-Beats-100

"""
Time Complexity : O(4^N*N), where N, is the length of input string.
 4^N for building every possible string combination and N to form the
  string by joining each character.. Here, 4 is chosen assuming the worst 
  case where each digit will be 7 or 9 and we would have 4*4*4*4 total string combinations.
Space Complexity : O(N), the max recursion depth will be N, where N is the length
 of input string. If the space required for ans is considered as well, the complexity will be O(4^N).
"""
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
        