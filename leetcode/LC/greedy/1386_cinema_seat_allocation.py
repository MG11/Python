from typing import List
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        data = defaultdict(set)
        
        for seat in reservedSeats:
            if seat[1] in {2,3,4,5}:
                data[seat[0]].add(0)
            if seat[1] in {4,5,6,7}:
                data[seat[0]].add(1)
            if seat[1] in {6,7,8,9}:
                data[seat[0]].add(2)
        res = 2*n	
        for i in data:
            if len(data[i]) == 3:
                res -= 2
            else:
                res -= 1
        return res
		
    
        # count = 0
        # print(data)
        # for i in range(1, n+1):
        #     seats = data.get(i, {})
        #     if len(seats) == 0:
        #         count += 2
        #     elif len(seats) == 1 or len(seats) == 2:
        #         count += 1
        # return count
