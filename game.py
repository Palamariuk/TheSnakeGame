from snake import *
from field import *
import pygame
import time

pygame.init()

class Game(Snake, Field):

    def __init__(self, width, height, bl_size):
        Snake.__init__(self, width // 2, height // 2)
        Field.__init__(self, width, height)
        self.bl_size = bl_size
        self.current_score = 0
        self.win_game = False

    def draw(self, screen, offset):
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.foodX * self.bl_size + offset, self.foodY * self.bl_size + offset, self.bl_size, self.bl_size))
        for block in self.snake:
            pygame.draw.rect(screen, (0, 255, 0),
                             (block[0] * self.bl_size + offset, block[1] * self.bl_size + offset, self.bl_size, self.bl_size))
        pygame.draw.rect(screen, (0, 190, 100),
                         (self.snake[0][0] * self.bl_size + offset, self.snake[0][1] * self.bl_size + offset, self.bl_size, self.bl_size))
        self.draw_border(screen, offset)
        self.draw_grid(screen, offset)
        text = 'Current score: ' + str(self.current_score)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        screen.blit(font.render(text, False, (255, 255, 255)), (offset, self.height * self.bl_size + 2 * offset))

        pygame.display.update()

    def draw_border(self, screen, offset):
        pygame.draw.line(screen, (255, 255, 255),
                         (offset, offset),
                         (self.width * self.bl_size + offset, offset),
                         2)
        pygame.draw.line(screen, (255, 255, 255),
                         (offset, self.height * self.bl_size + offset),
                         (self.width * self.bl_size + offset, self.height * self.bl_size + offset),
                         2)
        pygame.draw.line(screen, (255, 255, 255),
                         (offset, offset),
                         (offset, self.height * self.bl_size + offset),
                         2)
        pygame.draw.line(screen, (255, 255, 255),
                         (self.width * self.bl_size + offset, offset),
                         (self.width * self.bl_size + offset, self.height * self.bl_size + offset),
                         2)

    def draw_grid(self, screen, offset):
        for x in range(1, self.width):
            pygame.draw.line(screen, (50, 50, 50),
                             (x * self.bl_size + offset, offset),
                             (x * self.bl_size + offset, self.height * self.bl_size + offset),
                             1)
        for y in range(1, self.height):
            pygame.draw.line(screen, (50, 50, 50),
                             (offset, y * self.bl_size + offset),
                             (self.width * self.bl_size + offset, y * self.bl_size + offset),
                             1)

    def start_game(self):
        self.spawn_food()
        pygame.init()
        pygame.display.set_caption('TheSnakeGame')
        offset = self.bl_size
        screen = pygame.display.set_mode((self.width * self.bl_size + 2 * offset, self.height * self.bl_size + 4 * offset))

        while self.is_alive:
            self.draw(screen, offset)
            self.read_key()
            self.next_move()
            self.out_of_edge()
            self.eat()
            self.check_death()
            time.sleep(0.075)
        time.sleep(3)


    def spawn_food(self) -> None:
        while True:
            self.random_food()
            if((self.foodX, self.foodY) not in self.snake):
                break

    def out_of_edge(self):
        x = self.snake[0][0] % self.width
        y = self.snake[0][1] % self.height
        self.snake[0] = (x, y)

    def eat(self):
        if(self.snake[0] == (self.foodX, self.foodY)):
            self.current_score += 1
            self.inc_size()
            self.spawn_food()
        else:
            pass

    def read_key(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.is_alive = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if(self.direction != Direction.RIGHT):
                        self.change_dir(Direction.LEFT)
                if event.key == pygame.K_RIGHT:
                    if (self.direction != Direction.LEFT):
                        self.change_dir(Direction.RIGHT)
                if event.key == pygame.K_UP:
                    if (self.direction != Direction.DOWN):
                        self.change_dir(Direction.UP)
                if event.key == pygame.K_DOWN:
                    if(self.direction != Direction.UP):
                        self.change_dir(Direction.DOWN)
                if event.key == pygame.K_ESCAPE:
                    self.is_alive = False
