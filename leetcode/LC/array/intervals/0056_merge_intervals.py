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


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
