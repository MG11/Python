class Solution:
    def minimizeResult(self, expression: str) -> str:
        left_str, right_str = expression.split("+")
        min_val = float('inf')
        best_expr = ""

        for i in range(len(left_str)):
            for j in range(1, len(right_str) + 1):
                # Extract the four string components
                m1 = left_str[:i]
                a1 = left_str[i:]
                a2 = right_str[:j]
                m2 = right_str[j:]

                # Convert to integers, defaulting empty multipliers to 1
                mult1 = int(m1) if m1 else 1
                add1 = int(a1)
                add2 = int(a2)
                mult2 = int(m2) if m2 else 1

                current_val = mult1 * (add1 + add2) * mult2

                # Immediately format and save the exact string representation
                if current_val < min_val:
                    min_val = current_val
                    best_expr = f"{m1}({a1}+{a2}){m2}"

        return best_expr