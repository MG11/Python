from typing import List

#  here rows are sorted and columns are sorted independently, take top right element and check if traverse left 
# or bottom until target is found
# TC O(m + n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0 # row
        j = len(matrix[0]) - 1 # col
        
        while( i < len(matrix) and j >= 0):
            if(target == matrix[i][j]):
                return True
            elif(target < matrix[i][j]):
                j -= 1
            else:
                i += 1
        return False
        