# O(nlogk) | O(k) where n is number of type of words

from functools import total_ordering
from collections import defaultdict
from typing import List
import heapq

@total_ordering
class Element:
    def __init__(self, key, count):
        self.key = key
        self.count = count
    
    def __lt__(self, other):
        # ex: i : 2, love: 2 in this love is higher, as with same count we have to exclude words with higher order
        # the one having bigger key is considered less if having same count
        if self.count == other.count:
            return self.key > other.key
        return self.count < other.count
    
    def __eq__(self, other):
        return self.key == other.key and self.count == other.count
    

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        
        heaplist = []
        heapq.heapify(heaplist)
        for key, value in count.items():
            heapq.heappush(heaplist, (Element(key, value)))
            if len(heaplist) > k:
                heapq.heappop(heaplist)
        ans = []
        
        for elements in range(k):
            element = heapq.heappop(heaplist)
            ans.append(element.key)
        
        ans.reverse()
        return ans
        