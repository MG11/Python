class Solution:
# Complexity: Time O(n^2), Space O(1)
# Explanation: 2 nested loops found -> O(n^2); no obvious large temporary structures
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r)//2
            hour = 0
            for pile in piles:
                hour +=  math.ceil(pile/k)
            if hour > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
        return res
