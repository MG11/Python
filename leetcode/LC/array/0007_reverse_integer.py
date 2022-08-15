import math

class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        while(x):
            q = int(math.fmod(x, 10)) # quotient -1 %10 = 9
            x = int(x/10) # divide by 10, -1 // 10 = -1
            maximum = 2**31 -1
            minimum = -2**31
            if(sum > maximum//10 or (sum == maximum//10 and  q > maximum%10)):
                return 0
            if(sum < minimum//10 or (sum == minimum//10 and q < minimum%10)):
                return 0
            sum = sum*10 + q
        return sum
        