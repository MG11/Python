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


"""
The time complexity depends on how many stepping numbers exist up to high (at most 2 × 10⁹, i.e., 10 digits).

Counting stepping numbers by digit length:

1 digit: 10 numbers (0–9)
k digits: each stepping number branches into at most 2 children (last digit ± 1), so there are at most ~10 × 2^(k-1) stepping numbers with k digits
Total stepping numbers up to 10 digits:
10+10×2+10×2 
2
 +⋯+10×2 
9
 ≈10×2 
10
 ≈10,240

This is a very small number — the BFS visits at most ~O(2^d) nodes where d is the number of digits (at most 10).

Per node: O(1) work (check last digit, enqueue up to 2 children).

Sorting the result: O(S log S) where S ≤ ~10,240.

Overall: O(2^d + S log S) — effectively O(1) since d ≤ 10 is bounded by the constraint.
"""
        
