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

"""
https://www.youtube.com/watch?v=UcoN6UjAI64&list=PL-CpLXmniLM0-qfEtmKgX95XtTU8npTX6&index=4

The final approach to solving the Reverse Bits problem uses bit manipulation to efficiently reverse the 32 bits of an unsigned integer in O(1) time and space complexity.
"""
