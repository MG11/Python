import heapq
from typing import List

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.temp = nums[:]
        heapq.heapify(self.temp)
        self.k = k
        while(len(self.temp) > k):
            heapq.heappop(self.temp)
        
    
    def add(self, val: int) -> int:
        heapq.heappush(self.temp, val)
        if(len(self.temp) > self.k):
            heapq.heappop(self.temp)
        return self.temp[0]
        