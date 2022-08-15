# O(log3*n) + O(n) | O(3)
"""
add count and character in priority queue, of last and second last
are same the pop one more alphabet and add that
"""
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heaplist = []
        res = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heaplist.append((count, char))
        
        heapq.heapify(heaplist)
        # log3 * n
        while len(heaplist):
            count, char = heapq.heappop(heaplist)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if len(heaplist):
                    count1, char1 = heapq.heappop(heaplist)
                    res.append(char1)
                    count1 += 1
                    if count1:
                        heapq.heappush(heaplist, (count1, char1))
                else:
                    break
            else:
                res.append(char)
                count += 1
            if count:
                heapq.heappush(heaplist, (count, char))
        return ''.join(res) # O(n)
