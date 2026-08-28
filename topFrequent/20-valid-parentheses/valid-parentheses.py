class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c in mapping and stack and stack[-1] == mapping.get(c):
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
