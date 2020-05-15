import pygame
from snake import config
from snake.draw import draw_rect
from snake.body import Snake
from snake.food import Food

width = config.screen["caption_width"]
height = config.screen["caption_height"]
black = config.snake_color["black"]
yellow = config.snake_color["yellow"]
green = config.snake_color["green"]
white = config.snake_color["white"]
game_title = "hungry snake"

# create Snake object
snake = Snake(width, height)
# create food object
food = Food()

cell = 10
pygame.init()
caption = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_title)


def init():
	caption.fill(black)
	draw_rect(caption, white, food.food_pos)
	draw_rect(caption, green, snake.head_pos)
	draw_rect(caption, yellow, snake.body_pos)
	pygame.display.update()


while True:
	event = pygame.event.poll()
	init()
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			snake.change_direction("left", cell, food)
		elif event.key == pygame.K_RIGHT:
			snake.change_direction("right", cell, food)
		elif event.key == pygame.K_UP:
			snake.change_direction("up", cell, food)
		elif event.key == pygame.K_DOWN:
			snake.change_direction("down", cell, food)
	if snake.hit_self() or snake.hit_the_wall():
		print("game over")
		exit()
	if event.type == pygame.QUIT:
		print("game over")
		exit()



