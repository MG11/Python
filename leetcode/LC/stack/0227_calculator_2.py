# O(n) | O(1)
class Solution:
    def precedence(self, op):
        return op == '*' or op == '/'
    
    def evaluate(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        if op == '*':
            return num1*num2
        if op == '/':
            return num1//num2
            
    def calculate(self, s: str) -> int:
        op = []
        num = []
        operators = {'+', '-', '*', '/'}
        current = []
        for a in s+'+':
            if a in operators:
                num.append(int(''.join(current)))
                current = []
                while(len(op) and self.precedence(op[-1]) >= self.precedence(a)):
                    num2 = num.pop()
                    num1 = num.pop()
                    operator = op.pop()
                    result = self.evaluate(num1, num2, operator)
                    num.append(result)
                op.append(a)
            else:
                current.append(a)
        return num[-1]
                