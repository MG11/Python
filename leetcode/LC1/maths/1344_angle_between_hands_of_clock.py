class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_degree = minutes*6
        hour_degree = (hour%12)*30
        hour_by_minute = minute_degree/12
        degree = abs(hour_degree + hour_by_minute - minute_degree)
        degree = degree if degree < 180 else abs(degree-360)
        return degree
        