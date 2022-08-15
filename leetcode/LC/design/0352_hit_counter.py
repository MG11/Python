"""
1) use deque
2) use dictionary
3) use array

use threading:
import threading
lock = threading.Lock()
lock.acquire()
lock.release()

https://leetcode.com/problems/design-hit-counter/discuss/83511/Python-solution-with-detailed-explanation
"""


class HitCounter:

    def __init__(self):
        self.arr = [(0,0)]*301 # 0th for index, 1th for hit count
        
    def hit(self, timestamp: int) -> None:
        time = timestamp%300
        idx, hit = self.arr[time]
        if idx == timestamp:
            self.arr[time] = timestamp, hit +1
        else:
            self.arr[time] = timestamp, 1
        

    def getHits(self, timestamp: int) -> int:
        count = 0
        for counter in self.arr:
            if timestamp - 300 < counter[0] <= timestamp:
                count += counter[1]
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)