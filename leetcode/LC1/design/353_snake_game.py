from typing import List
from collections import deque

class SnakeGame:
    
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        food.reverse()
        self.food = food
        self.snake = deque()
        self.score = 0
        self.snake.append((0,0))
        self.snakeset = {(0,0),}
        self.moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        
    def move(self, direction: str) -> int:
        current_food = self.food[-1] if self.food else None
        move = self.moves.get(direction)
        r, c = self.snake[-1][0] + move[0], self.snake[-1][1] + move[1]
        if (r,c) in self.snakeset and (r,c) != self.snake[0]:
            return -1
        if(r < 0 or r >= self.height or c < 0 or c >= self.width):
            return -1
        if current_food and current_food[0] == r and current_food[1] == c:
            self.food.pop()
            self.score += 1
        else:
            tail = self.snake[0]
            self.snakeset.remove(tail)
            self.snake.popleft()
        self.snakeset.add((r,c))
        self.snake.append((r,c))
        return self.score
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)