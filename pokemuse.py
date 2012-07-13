import pygame
from pygame.locals import *

pygame.init()

game_window = pygame.display.set_mode((640, 480))
fps_clock = pygame.time.Clock()

while True:

    pygame.display.update()
    fps_clock.tick(30)
