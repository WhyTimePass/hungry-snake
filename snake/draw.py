"""
pygame draw action
"""

import pygame
from snake import config


def draw_rect(caption, color, position):
    cell = config.screen["cell"]
    if len(position) == 2:
        pygame.draw.rect(caption, color,
                         pygame.Rect(position[0], position[1], cell, cell))
    else:
        for pos in list(position)[:-1]:
            pygame.draw.rect(caption, color,
                             pygame.Rect(pos[0], pos[1], cell, cell))
