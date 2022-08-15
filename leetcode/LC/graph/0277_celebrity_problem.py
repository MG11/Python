# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
"""
https://leetcode.com/problems/find-the-celebrity/solution/
approach 2
O(3*n) | O(1)
"""
def knows(a, b):
    return True
    
class Solution:
    def __init__(self):
            self.n = 0
            
    def findCelebrity(self, n: int) -> int:
        self.n = n
        possible = 0
        # find possible celebrity 
        # if possible knows i then possible can't be celebrity
        for i in range(n):
            if(knows(possible, i)):
                possible = i
                
        if(self.iscelebrity(possible)):
            return possible
        return -1
    
    def iscelebrity(self, possible):
        # only possible can be celebrity and no one else
        # check if everyone knows celebrity, and celebrity knows no one
        for i in range(self.n):
            if(i == possible):
                continue
            if not knows(i, possible) or knows(possible, i):
                return False
        return True
        