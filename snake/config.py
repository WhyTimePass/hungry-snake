"""
snake config
"""
import pygame


class BaseConfig:
    caption_width = 500
    caption_height = 500
    cell = 10
    foods = (255, 0, 0)
    head = (255, 255, 0)
    body = (0, 128, 0),
    bg = (200, 200, 200)
    game_title = "hungry snake"
    caption = pygame.display.set_mode((caption_width, caption_height))
    clock = pygame.time.Clock()