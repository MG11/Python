class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                output = []
                while stack[-1] != '[':
                    output.append(stack[-1])
                    stack.pop()
                else:
                    stack.pop()
                output.reverse()
                numstr = ""
                while stack and stack[-1].isdigit():
                    numstr= stack.pop() + numstr
                    
                count = int(numstr) if numstr else 1
                stack.extend(output*int(count))
            else:
                stack.append(c)
        ans = "".join(stack)
        return ans
