from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0]*3
        cols = [0]*3
        diagonal = 0
        anti_diagonal = 0
        player = 1
        player_name = {1: 'A', 0: 'B'}
        
        for move in moves:
            count = 1 if player == 1 else -1
            r, c = move[0], move[1]
            rows[r] += count
            cols[c] += count
            if(r + c == 2):
                anti_diagonal += count
            if(r == c):
                diagonal += count
            player = 1 - player
        r, c = moves[-1][0], moves[-1][1]
        results = (rows[r], cols[c], diagonal, anti_diagonal)
        for result in results:
            if result == 3:
                return 'A'
            if result == -3:
                return 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'
