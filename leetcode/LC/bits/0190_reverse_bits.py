# https://www.youtube.com/watch?v=FMdQxjiqg2I

"""
for 8 bits:
0 0 0 0 0 1 0 1 

"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if((1 << i) & n): 
                res = res | (1 << (32 - i - 1))
        return res

