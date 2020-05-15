"""
snake food
"""

import random


class Food:
    def __init__(self):
        self.food_pos = [random.randrange(1, 50) * 10,
                         random.randrange(1, 50) * 10]

    def rebuild(self):
        self.food_pos = [random.randrange(1, 50) * 10,
                         random.randrange(1, 50) * 10]

