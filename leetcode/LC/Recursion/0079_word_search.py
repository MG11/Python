from typing import List

# https://leetcode.com/problems/word-search/discuss/747144/Python-dfs-backtracking-solution-explained

"""
Complexity: Time complexity is potentially O(m*n*3^k), where k is length of word and m and n
are sizes of our board: we start from all possible cells of board, and each time (except first)
we can go in 3 directions (we can not go back). In practice however this number will be usually
much smaller, because we have a lot of dead-ends. Space complexity is O(k), k is length of word.
"""
class Solution:
    def dfs(self, board, r, c, word, index):
        if(len(word) == index):
            return True
        # if value it the board cell is not equal to the word's index
        if board[r][c] != word[index]:
            return False
        # set value to # so, that we dont do dfs on it again         
        value = board[r][c]
        board[r][c] = '#'
        # if we are at last index and value of alphabet is as expected, return true         
        if word[index] == word[-1] and index == len(word) -1:
            return True
        # do dfs in all 4 directions for the pending alphabets in word         
        for d in [(r, c+1), (r+1, c), (r-1, c), (r, c-1)]:
            ans = False
            if  0 <= d[0] < len(board) and 0 <= d[1] < len(board[0]) and not board[d[0]][d[1]] == '#':
                currentAns = self.dfs(board, d[0], d[1], word, index+1)
                if currentAns:
                    return True
        # for the value changed to # revert it back to original value         
        board[r][c] = value
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, r, c, word, 0):
                    return True
        return False


class Solution:
    def __init__(self):
        self.word = None
        self.board = None
        
    def dfs(self, i, j, index):
        if index == len(self.word) - 1 and self.board[i][j] == self.word[-1]:
            return True
        if self.board[i][j] != self.word[index]:
            return False
        value = self.board[i][j]
        self.board[i][j] = '#'
        directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        
        for d in directions:
            if 0 <= d[0] < len(self.board) and 0 <= d[1] < len(self.board[0]) and self.board[d[0]][d[1]] != '#':
                value1 = self.board[d[0]][d[1]]
                result = self.dfs(d[0], d[1], index+1)
                if result:
                    self.board[d[0]][d[1]] = value1
                    return True
        self.board[i][j] = value
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        self.word = word
        self.board = board
        for i in range(row):
            for j in range(col):
                if self.dfs(i, j ,0):
                    return True
        return False
        