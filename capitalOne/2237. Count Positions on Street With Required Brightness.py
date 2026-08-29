class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        
        sum = [0]*(n+1)
        for light in lights:
            leftRange = max(0, light[0] - light[1])
            rightRange = min(n - 1, light[0] + light[1])
            sum[leftRange] += 1
            sum[rightRange + 1] -= 1

        for i in range(1, n + 1):
            sum[i] += sum[i-1]


        count = 0
        for i in range(n):
            if requirement[i] <= sum[i]:
                count += 1
        return count

"""
Difference Array (Line Sweep) Algorithm

Use this approach for range update problems to avoid Time Limit Exceeded (TLE) errors.

• The Core Idea: Instead of using a nested loop to update every element in a range `[L, R]`, you only record the boundary events.

• Start Point: `diff[L] += 1` (The coverage begins here).

• End Point: `diff[R + 1] -= 1` (The coverage definitively stops here).

• The Sweep: Iterate through the array once, keeping a running sum. The running sum at any index gives you the exact count of overlapping ranges at that specific point.

• Complexity: Reduces time complexity from $O(L \times N)$ to $O(L + N)$.

• The Bus Analogy: `+1` is passengers boarding the bus, `0` is driving past stops with no changes (carrying the previous count forward), and `-1` is passengers getting off.

"""
