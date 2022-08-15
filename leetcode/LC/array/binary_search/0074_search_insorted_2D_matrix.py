from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        start = 0
        end = row*col - 1
        
        while(start <= end):
            mid = (start + end)//2
            r = mid//col
            c = mid%col
            if(matrix[r][c] == target):
                return True
            if(matrix[r][c] < target):
                start = mid +1
            else:
                end = mid - 1
        return False
        