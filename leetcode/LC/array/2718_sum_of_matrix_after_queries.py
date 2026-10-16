from typing import List


class Solution:
    def sumOfMatrixAfterQueries(self, n: int, queries: List[List[int]]) -> int:
        total = n * n
        seen = set()
        row = [False] * n
        col = [False] * n
        ans = 0

        for index, value in queries:
            if index < n:
                if not row[index]:
                    row[index] = True
                    ans += (n - sum(col)) * value
                    total -= n - sum(col)
            else:
                j = index - n
                if not col[j]:
                    col[j] = True
                    ans += (n - sum(row)) * value
                    total -= n - sum(row)
        return ans
