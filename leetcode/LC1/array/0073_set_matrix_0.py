from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        colzero = False
        rowzero = False
        
        # if first row or first col is zero set rowzero and colzero to true,
        # if anyvalue is zero, set its respective first row and col value to zero
        for i in range(row):
            for j in range(col):
                if(matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        rowzero = True
                    if j == 0:
                        colzero = True
        
        # using those first row and col value set all other values to 0
        for i in range(1,row):
            for j in range(1,col):
                if(matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
        
        # set value to 0 in all first col
        if colzero:
            for i in range(row):
                matrix[i][0] = 0
        
        # set value to 0 in all first row
        if rowzero:
            for i in range(col):
                matrix[0][i] = 0
        