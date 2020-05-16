import pygame
from snake.game import Rule

action = None
if __name__ == "__main__":
	Rule.init(pygame)
	while True:
		event = pygame.event.poll()
		Rule.update(pygame)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				action = "left"
			elif event.key == pygame.K_RIGHT:
				action = "right"
			elif event.key == pygame.K_UP:
				action = "up"
			elif event.key == pygame.K_DOWN:
				action = "down"
			elif event.key == pygame.K_SPACE and Rule.dead:
				Rule.restart()
				action = "right"
		Rule.move(action)
		if Rule.snake_dead():
			Rule.dead_status()
		if event.type == pygame.QUIT:
			exit()
