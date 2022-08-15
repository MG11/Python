from typing import List

# https://leetcode.com/problems/word-search/discuss/747144/Python-dfs-backtracking-solution-explained

"""
Complexity: Time complexity is potentially O(m*n*3^k), where k is length of word and m and n
are sizes of our board: we start from all possible cells of board, and each time (except first)
we can go in 3 directions (we can not go back). In practice however this number will be usually
much smaller, because we have a lot of dead-ends. Space complexity is O(k)
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
