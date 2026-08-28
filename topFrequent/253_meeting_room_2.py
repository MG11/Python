class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        
        intervals.sort()
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
            print(heap)
        return len(heap)
            
