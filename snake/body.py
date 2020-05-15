"""
Snake body
"""
from collections import deque


class Snake:
    cell = 10

    def __init__(self, width, height):
        self.body_pos = deque([k * 10, 250] for k in range(26)[-4:])
        self.head_pos = self.body_pos[-1]
        self.width = width
        self.height = height

    def hit_self(self):
        return True if self.head_pos in list(self.body_pos)[:-1] else False

    def hit_the_wall(self):
        return True if self.head_pos[0] >= self.width or self.head_pos[0] < 0 \
                       or self.head_pos[1] >= self.height or self.head_pos[1] \
                       < 0 else False

    def change_direction(self, direct, cell, food):
        val = list(self.head_pos)
        if direct == "up":
            val[1] -= cell
        elif direct == "down":
            val[1] += cell
        elif direct == "left":
            val[0] -= cell
        elif direct == "right":
            val[0] += cell
        self.head_pos = val
        self.body_pos.append(val)
        self.body_pos.popleft() if food.food_pos != val else food.rebuild()


