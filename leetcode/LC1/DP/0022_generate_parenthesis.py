from typing import List

class Solution1:
    def __init__(self):
        self.arr = []
    def backtrackPar(self, ans, open, close):
        if(open == close == 0):
            self.arr.append(ans) 
            return
        if(open == close):
            self.backtrackPar(ans + "(", open -1, close)
        if(open < close):
            self.backtrackPar(ans + ")", open, close -1)
            if(open != 0):
                self.backtrackPar(ans + "(", open -1, close)
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrackPar("", n,n)
        return self.arr
    
class Solution:
    def __init__(self):
        self.arr = []
    def backtrackPar(self, ans, open, close, n):
        if(open == close == n):
            self.arr.append(ans) 
            return
        if(open == close):
            self.backtrackPar(ans + "(", open +1, close, n)
        if(open > close):
            self.backtrackPar(ans + ")", open, close +1, n)
            if(open != n):
                self.backtrackPar(ans + "(", open +1, close, n)
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrackPar("", 0,0, n)
        return self.arr
        