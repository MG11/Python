class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        val = 1
        for i in range(32):
            bit = n & val
            val = val << 1
            if bit:
                res = res | (1 << (31 - i))
        return res
