import heapq
from typing import List

class Solution:
    def connectSticks(self, stick: List[int]) -> int:
        if(len(stick) == 1):
            return 0
        ans = 0
        heapq.heapify(stick)
        while(len(stick) != 1):
            small = heapq.heappop(stick)
            big = heapq.heappop(stick)
            ans += small + big
            heapq.heappush(stick, small + big)
        return ans
