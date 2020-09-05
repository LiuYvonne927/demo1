import pygame
pygame.init()
import random

window_size = [800,600]
screen = pygame.display.set_mode(window_size)

image = pygame.image.load('./duck.png')
screen.bilt(image,(0,0))

is_game_over = False

while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()

    pygame.display.flip()

pygame.quit()