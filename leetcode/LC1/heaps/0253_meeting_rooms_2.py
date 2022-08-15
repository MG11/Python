import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if(len(intervals) == 0):
            return 0
        intervals.sort() # sort the array on thr basis of start time
        heaplist = [intervals[0][1]] # take min heap and push first meeting end time
        heapq.heapify(heaplist) # heapify that list
        rooms = 1
        for i in range(1, len(intervals)):
            # compare minimum end time of any room ( which will be at top), comprre it with current room end time.
            if(heaplist[0] <= intervals[i][0]):
                heapq.heappop(heaplist)
            else:
                rooms += 1

            # insert current room end time
            heapq.heappush(heaplist, intervals[i][1])
        return rooms
    