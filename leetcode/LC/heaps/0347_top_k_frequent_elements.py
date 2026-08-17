"""
The heapq documentation suggests that heap elements could be tuples in which the first element is the priority and defines the sort order.

"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = Counter(nums)

        heap = []

        for (key, val) in data.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [key for (val, key) in heap]

    
