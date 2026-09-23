class Solution:
    def compress(self, chars: list[str]) -> int:
        output = []
        count = 1
        current_char = chars[0]
        for c in chars[1:]:
            if c == current_char:
                count += 1
            else:
                output.append(current_char)
                output.append(str(count)) if count > 1 else None
                current_char = c
                count = 1
        output.append(current_char)
        output.append(str(count)) if count > 1 else None
        ans = ''.join(output)
        output = list(ans)
        chars[:len(output)] = output
        return len(ans)
