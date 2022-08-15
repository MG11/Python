import heapq
import imp
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        heaplist = []
        
        for key, value in frequency.items():
            heapq.heappush(heaplist, (value,key))
            if len(heaplist) > k:
                heapq.heappop(heaplist)
        result = []
        for data in heaplist:
            result.append(data[1])
        return result
