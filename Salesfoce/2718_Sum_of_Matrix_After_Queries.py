class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        total = 0
        l = len(queries)
        data = set()
        row_covered, col_covered = 0, 0
        for i in range(l -1, -1, -1):
            q = queries[i]
            position = (q[0], q[1])
            if position in data:
                continue
            else:
                data.add(position)
                if q[0] == 1:
                    total += (n - row_covered)*q[2]
                    col_covered += 1
                else:
                    total += (n - col_covered)*q[2]
                    row_covered += 1
        return total
