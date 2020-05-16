import pygame

pygame.font.init()
font = pygame.font.SysFont('simhei', 24)


def score_count(caption, snake):
	score_text = "score: " + str(snake.count)
	score = font.render(score_text, True, (0, 0, 0))
	score_rect = score.get_rect()
	score_rect.centerx = caption.get_rect().centerx
	score_rect.y = 10
	caption.blit(score, score_rect)


def summary(caption, snake):
	draw_text = "Your score is: " + str(snake.count) + " and press space restart"
	text = font.render(draw_text, True, (255, 255, 255))
	text_rect = text.get_rect()
	text_rect.center = caption.get_rect().center
	caption.blit(text, text_rect)
	pygame.display.flip()