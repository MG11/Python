# https://leetcode.com/problems/non-overlapping-intervals/discuss/?currentPage=1&orderBy=most_votes&query=

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort on end index because we should keep room with small size
        """
        ex: 1 3   1 2   2 3   3 4 : we discard rooms first and second to keep room 0th
            1 2   2 3   1 3   3 4 : we discard only room 1 3 
        """
        intervals.sort(key=lambda x : x[1])
        
        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if (intervals[i][0] < end):
                count += 1
            else:
                end = intervals[i][1]
        return count
    