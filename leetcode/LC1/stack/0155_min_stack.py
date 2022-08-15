import sys

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # push tuple of current value and minimum value till num
        if len(self.stack) == 0:
            minimum = val
        else:
            minimum = min(self.stack[-1][1], val)
        self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()
        return None

    def top(self) -> int:
        if(len(self.stack)):
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if(len(self.stack)):
            return self.stack[-1][1]
        return None
        