class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list[int]:
        ans = set()
        q = deque(range(10))

        while q:
            e = q.popleft()
            if low <= e <= high:
                ans.add(e)
            
            if e < high:
                d = e % 10
                if d == 0:
                    q.append(e*10 + 1) if e*10 + 1 <= high else None
                elif d == 9:
                    q.append(e*10 + 8) if e*10 + 8 <= high else None
                else:
                    q.append(e*10 + d + 1) if e*10 + d + 1 <= high else None
                    q.append(e*10 + d - 1) if e*10 + d - 1 <= high else None
        return sorted(ans)
        