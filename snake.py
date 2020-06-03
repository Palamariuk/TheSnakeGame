from enum import Enum

Direction = Enum('Direction', 'UP DOWN LEFT RIGHT')

class Snake:
    snake = []
    is_alive = True
    direction = Direction.UP
    size = 3

    def __init__(self, head_x, head_y):
        self.snake = [(head_x, head_y + i) for i in range(self.size)]

    def next_move(self):
        if(self.direction == Direction.UP):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 1))
        elif (self.direction == Direction.DOWN):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 1))
        elif (self.direction == Direction.LEFT):
            self.snake.insert(0, (self.snake[0][0] - 1, self.snake[0][1]))
        elif (self.direction == Direction.RIGHT):
            self.snake.insert(0, (self.snake[0][0] + 1, self.snake[0][1]))
        self.snake.pop(len(self.snake) - 1)

    def change_dir(self, direction):
        self.direction = direction

    def inc_size(self):
        self.snake.append(self.snake[len(self.snake) - 1])
        self.size += 1

    def check_death(self):
        for i in range(1, len(self.snake)):
            if(self.snake[0] == self.snake[i]):
                self.is_alive = False
