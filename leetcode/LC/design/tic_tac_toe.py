# O(1) | O(n)
class TicTacToe:

    def __init__(self, n: int):
        self.row = [0]*n
        self.col = [0]*n
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.row)
        player = 1 if player == 1 else -1
        self.row[row] += player
        self.col[col] += player
        self.diagonal += player if row == col else 0
        self.antidiagonal += player if row + col == n - 1 else 0
        
        for x in [self.row[row], self.col[col], self.diagonal, self.antidiagonal]:
            if x == n:
                return 1
            elif x == -n:
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
    
    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
