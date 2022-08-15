class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        count = 0
        currentstr = ''
        for i in s:
            if i.isdigit():
                count = count*10 + int(i)
            elif i == '[':
                stack.append(currentstr)
                stack.append(count)
                currentstr = ''
                count = 0 # count digit
            elif i == ']':
                prevnum = stack.pop()
                prevstr = stack.pop()
                currentstr = prevstr + prevnum*currentstr
            else:
                currentstr += i # create string
        return currentstr
                