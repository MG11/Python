"""
Adding a number num:

Add num to max-heap lo. Since lo received a new element, we must do a balancing step for hi.
 So remove the largest element from lo and offer it to hi.
The min-heap hi might end holding more elements than the max-heap lo, after the previous operation.
 We fix that by removing the smallest element from hi and offering it to lo.

refer LC solution
"""
import heapq

class MedianFinder:

    def __init__(self):
        self.size = 0
        self.maxheap = []
        self.minheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)
     
    def addNum(self, num: int) -> None:
        if self.maxheap and num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        elif self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        # balance
        # maxheaplength: 2, minheaplength: 0
        if len(self.maxheap) - len(self.minheap) > 1:
            x = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -x)
        
        # maxheaplength: 1, minheaplength: 2
        if len(self.minheap) - len(self.maxheap) >= 1:
            x = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -x)
        self.size += 1
        

    def findMedian(self) -> float:
        if self.size == 0:
            return 0
        if self.size %2 == 0:
            return (self.minheap[0] - self.maxheap[0])/2
        else:
            return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()