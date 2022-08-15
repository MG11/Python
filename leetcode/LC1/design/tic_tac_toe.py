class TicTacToe:
    
    # refer c++ solution from leetcode solutions
    def __init__(self, n: int):
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = 0
        self.anti_diagonal = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        ans = 1 if player == 1 else -1
        n = len(self.rows)
        self.rows[row] += ans
        self.cols[col] += ans
        if row == col:
            self.diagonal += ans
        if row + col == n -1:
            self.anti_diagonal += ans
        result = [self.rows[row], self.cols[col], self.diagonal, self.anti_diagonal]
        for x in result:
            if(x == n):
                print(result)
                return 1
            if (x == -n):
                return 2
        return 0
    
    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
