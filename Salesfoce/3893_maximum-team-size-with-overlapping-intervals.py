import bisect

class Solution:
    def maximumTeamSize(self, startTime: list[int], endTime: list[int]) -> int:
        start = sorted(startTime)
        end = sorted(endTime)

        maxteam = 0
        for s, e in zip(startTime, endTime):
            a = bisect_right(start, e)
            b = bisect_left(end, s)
            maxteam = max(maxteam, (a - b))
        return maxteam
