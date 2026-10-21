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
                    q.append(e*10 + 1)
                elif d == 9:
                    q.append(e*10 + 8)
                else:
                    q.append(e*10 + d + 1)
                    q.append(e*10 + d - 1)
        return sorted(ans)
        