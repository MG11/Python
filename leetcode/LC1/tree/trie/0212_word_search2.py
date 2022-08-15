from typing import List

# https://leetcode.com/problems/word-search-ii/discuss/712733/Python-Trie-solution-with-dfs-explained

class Trie:
    
    def __init__(self):
        self.data = {} # key as word value as trie node
        self.end = False
    
    def insert(self, word):
        Node = self
        for w in word:
            if Node.data.get(w):
                Node = Node.data.get(w)
            else:
                Node.data[w] = Trie()
                Node = Node.data[w]
        Node.end = True

    
class Solution:
    def __init__(self):
        #  make pointer to board
        self.board = []
        # res to store result
        self.res = []
        self.num_words = 0
        
    def dfs(self, r, c, node, path):
        if not self.num_words:
            return
        # check if node data has the current board value
        node = node.data.get(self.board[r][c])
        if not node:
            return
        path += self.board[r][c]
        if node.end:
            self.res.append(path)
            # set node.end to false so that if same word is found 2 times in board we dont append it twice
            node.end = False
            self.num_words -= 1

            # make it visited so that we dont visit it again 
        self.board[r][c] = self.board[r][c].upper()
        for d in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
            if 0 <= d[0] < len(self.board) and 0 <= d[1] < len(self.board[0]):
                self.dfs(d[0], d[1], node, path)
        # again completing our dfs mark it unvisited so that it can be used later
        self.board[r][c] = self.board[r][c].lower()
            
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for i in range(len(words)):
            trie.insert(words[i])
        row = len(board)
        self.num_words = len(words)
        col = len(board[0])
        self.board = board
        for r in range(0,row):
            for c in range(0,col):
                self.dfs(r,c, trie, '')
        return self.res
    