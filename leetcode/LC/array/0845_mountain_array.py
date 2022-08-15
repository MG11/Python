# https://leetcode.com/problems/longest-mountain-in-array/solution/
# https://www.youtube.com/watch?v=h3st_zFMQNQ
# O(n) | O(1)

from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        max_length = 0
        if len(A) < 3:
            return 0
        i = 0
        peak, valley = False, False
        while(i < len(A) - 1):
            if(A[i] < A[i+1]):
                start = i
                while(i < len(A) - 1 and A[i] < A[i+1]):
                    peak = True
                    i += 1
                while(i < len(A) - 1 and A[i] > A[i+1]):
                    valley = True
                    i += 1
                if(peak and valley):
                    max_length = max(i - start + 1, max_length)
                peak = False
                valley = False
            else:
                i += 1
        return max_length
