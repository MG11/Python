class Solution:
    def minimizeResult(self, expression: str) -> str:
        leftExp, rightExp = expression.split("+")
        bestExp = ""
        minVal = float("inf")

        for i in range(len(leftExp)):
            for j in range(1, len(rightExp) + 1):

                m1 = leftExp[:i]
                add1 = leftExp[i:]
                add2 = rightExp[:j]
                m2 = rightExp[j:]

                mult1 = int(m1) if m1 else 1
                mult2 = int (m2) if m2 else 1
                add1 = int(add1)
                add2 = int(add2)

                value = mult1*(add1 + add2)*mult2

                if value < minVal:
                    bestExp = f"{m1}({add1}+{add2}){m2}"
                    minVal = value
        return bestExp
