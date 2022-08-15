from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first transpose the matrix and the roate by center column
        length = len(matrix)
        for row in range(length):
            # traverse till the diagonal only and swap the elements by corresponding col and row
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
         # transpose across the centre column, so, traverse till centre col - 1

        # if anti clockwise, transpose across centre row
        for row in range(length):
            for col in range(length//2):
                matrix[row][col], matrix[row][length - 1 - col] = matrix[row][length - 1 - col], matrix[row][col]
                