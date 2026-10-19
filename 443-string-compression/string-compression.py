class Solution:
    def addCount(self, output, count):
        countData = []
        while count:
            c = count % 10
            count = count // 10
            countData.append(str(c))
        countData = countData[::-1]
        output.extend(countData)

    def compress(self, chars: list[str]) -> int:
        output = []
        
        count = 1
        current_char = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == current_char:
                count += 1
            else:
                output.append(current_char)
                current_char = chars[i]
                self.addCount(output, count) if count > 1 else None
                count = 1
        else:
            output.append(current_char)
            self.addCount(output, count) if count > 1 else None
        chars[:len(output)] = output
        return len(output)
