from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        minr = 0
        my_ans = []
        maxr = len(matrix) - 1
        minc = 0
        maxc = len(matrix[0]) - 1
        dir = 0
        while(minr <= maxr and minc <= maxc):
            if (dir == 0):  # left to right
                for i in range(minc, maxc + 1):
                    my_ans.append(matrix[minr][i])
                minr += 1
            elif (dir == 1): # top to bottom
                for i in range(minr, maxr + 1):
                    my_ans.append(matrix[i][maxc])
                maxc -= 1
            elif(dir == 2): # right to left
                for i in range(maxc, minc -1, -1):
                    my_ans.append(matrix[maxr][i])
                maxr -= 1
            else: # bottom to top
                for i in range(maxr, minr -1, -1):
                    my_ans.append(matrix[i][minc])
                minc += 1
            dir = (dir +1)%4
        return my_ans
