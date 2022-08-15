"""
TC: klog(k)
SC: k
approach 1: pop k elements from list --> O(klogn)
approach 2: take another min heap (temp), push top element from current heap,
now, pop an element from temp and push its children k times..
top element will be the kth smallest. 
"""

import heapq

def findMin(data, k):
    heapq.heapify(data)
    temp = [[data[0],0]]
    heapq.heapify(temp)
    print(data)
    node = None
    while k:
        node = heapq.heappop(temp)
        l = 2*node[1] + 1
        r = 2*node[1] + 2
        if l < len(data):
            heapq.heappush(temp, [data[l], l])
        if r < len(data):
             heapq.heappush(temp, [data[r], r])
        k -=1
    return node[0]
            
data = [10, 50, 40, 45, 65, 75, 60, 65]
k = 3
print(findMin(data, k))
