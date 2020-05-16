from snake.config import BaseConfig
from snake.draw import draw_rect, draw_grid
from snake.body import Snake
from snake.food import Food
from snake.font import score_count, summary


class Rule(BaseConfig):
	action = "right"
	dead = False
	# create Snake object
	snake = Snake(BaseConfig.caption_width, BaseConfig.caption_width)
	# create food object
	food = Food()

	@classmethod
	def __draw_snake(cls):
		cls.caption.fill(cls.bg)
		draw_rect(cls.caption, cls.foods, cls.food.food_pos)
		draw_rect(cls.caption, cls.head, cls.snake.head_pos)
		draw_rect(cls.caption, cls.body, cls.snake.body_pos)
		draw_grid(cls.caption)
		score_count(cls.caption, cls.snake)
		# define speed
		cls.clock.tick(10)

	@staticmethod
	def init(pygame):
		pygame.init()
		pygame.display.set_caption(BaseConfig.game_title)
		Rule.__draw_snake()
		pygame.display.flip()

	@classmethod
	def update(cls, pygame):
		cls.__draw_snake()
		pygame.display.flip()

	@classmethod
	def dead_status(cls):
		summary(cls.caption, cls.snake)
		cls.cell = 0
		cls.dead = True

	@classmethod
	def restart(cls):
		cls.dead = False
		cls.cell = BaseConfig.cell
		cls.snake.clear()
		cls.food.rebuild()

	@classmethod
	def move(cls, direction=None):
		if not direction:
			direction = cls.action
		cls.snake.change_direction(direction, cls.cell, cls.food)

	@classmethod
	def snake_dead(cls):
		return True if cls.snake.hit_self() or cls.snake.hit_the_wall() else False
