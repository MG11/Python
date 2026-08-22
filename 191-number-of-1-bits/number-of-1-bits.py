class Solution:
    def hammingWeight(self, n: int) -> int:
        twopower = 0
        
        counter = 0
        while n:
            counter += n & 1
            n = n >> 1
            print(n)
        return counter
