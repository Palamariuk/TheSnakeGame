import random

class Field:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_food(self):
        self.foodX = random.randint(0, self.width - 1)
        self.foodY = random.randint(0, self.height - 1)
