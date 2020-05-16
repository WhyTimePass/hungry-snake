"""
pygame draw action
"""

import pygame
from snake.config import BaseConfig


def draw_rect(caption, color, position):
    cell = BaseConfig.cell
    if len(position) == 2:
        pygame.draw.rect(caption, color,
                         pygame.Rect(position[0], position[1], cell, cell))
    else:
        for pos in list(position)[:-1]:
            pygame.draw.rect(caption, color,
                             pygame.Rect(pos[0], pos[1], cell, cell))


def draw_grid(caption):
    row = 50
    col = 50
    color = (0, 200, 100)
    width = BaseConfig.caption_width
    height = BaseConfig.caption_height
    cell_width = width/col
    cell_height = height/row
    for r in range(row):
        pygame.draw.line(caption, color, (0, r * cell_height),
                         (width, r * cell_height))
    for c in range(col):
        pygame.draw.line(caption, color, (c * cell_width, 0),
                         (c * cell_width, height))