from typing import List

class Solution:
    operators = ["+", "-", "*", '/']
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in self.operators:
                stack.append(i)
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                result = self.perform(o1, o2, i)
                stack.append(result)
        return int(stack.pop())
    
    def perform(self,o1, o2, i):
        if i == '+':
            return int(o1) + int(o2)
        if i == '-':
            return int(o1) - int(o2)
        if i == '*':
            return int(o1)*int(o2)
        else:
            return int(o1) / int(o2)
