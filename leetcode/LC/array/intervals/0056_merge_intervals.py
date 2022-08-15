# sorting is required so that can be merged come together
# O(n) | O(n)
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for i in range(1, len(intervals)):
            if(ans[-1][1] < intervals[i][0]):
                # merging if start is greater than previous end
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans
