import pygame
import random


caption_width = 500
caption_height = 500
white_color = (255, 255, 255)
black_color = (0, 0, 0)
game_title = "hungry snake"
cell = 10
snake_init_pos = [[250, 250], [240, 250], [230, 250], [220, 250]]
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
pygame.init()
caption = pygame.display.set_mode((caption_width, caption_height))
pygame.display.set_caption(game_title)
head_pos = [250, 250]


def draw_rect(color, position):
    pygame.draw.rect(caption, color,
                     pygame.Rect(position[0], position[1], cell, cell))


def change_direction(head_pos):
    global food_pos
    snake_init_pos.insert(0, list(head_pos))
    if head_pos != food_pos:
        snake_init_pos.pop()
    else:
        food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]


def main():
    caption.fill(black_color)
    for pos in snake_init_pos:
        draw_rect(white_color, pos)
    draw_rect(white_color, food_pos)
    pygame.display.update()


def hit_the_self():
    return True if snake_init_pos[0] in snake_init_pos[1:] else False


def hit_the_wall(head_pos):
    return True if head_pos[0] >= caption_width or head_pos[0] < 0 or \
        head_pos[1] >= caption_height or head_pos[1] < 0 else False


while True:
    event = pygame.event.poll()
    main()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            head_pos[0] -= cell
            change_direction(head_pos)
        elif event.key == pygame.K_RIGHT:
            head_pos[0] += cell
            change_direction(head_pos)
        elif event.key == pygame.K_UP:
            head_pos[1] -= cell
            change_direction(head_pos)
        elif event.key == pygame.K_DOWN:
            head_pos[1] += cell
            change_direction(head_pos)
    if hit_the_self() or hit_the_wall(head_pos):
        print("game over")
        exit()
    if event.type == pygame.QUIT:
        print("game over")
        exit()
