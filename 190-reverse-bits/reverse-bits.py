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

The final approach to solving the Reverse Bits problem uses bit manipulation to efficiently reverse the 32 bits of an unsigned integer in O(1) time and space complexity (7:13 - 10:00):

Initialization: Start with a result variable initialized to 0, which will hold the reversed bits.
Iteration: Loop 32 times (for each bit position in the 32-bit integer) (7:27).
Extracting the Bit: In each iteration i, identify the current bit from the input n. This is done by shifting n to the right by i positions and performing a bitwise AND with 1 (7:44 - 8:27).
Placing the Bit: To reverse the order, shift the extracted bit to the left by 31 - i positions. This moves the first bit to the 31st position, the second to the 30th, and so on (8:57 - 9:17).
Updating Result: Use a bitwise OR operation to add this shifted bit into the result variable (9:27 - 9:36).



"""