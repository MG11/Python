from typing import List


# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if( n== 0 or n == 1 or n == 2):
            return n
        
        secondLast = 1
        Last = 2
        current = 0
        for i in range(n-2):
            current = secondLast + Last
            secondLast = Last
            Last = current
        return current


# https://www.youtube.com/watch?v=Y0lT9Fck7qI
class Solution1:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1

        while n != 1:
            sum = first + second
            second = first
            first = sum
            n -= 1
        return first
        
