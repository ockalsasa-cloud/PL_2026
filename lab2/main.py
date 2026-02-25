import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((500, 500))

YELLOW = (255, 220, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Жёлтая голова
    circle(screen, YELLOW, (250, 250), 180)
    circle(screen, BLACK, (250, 250), 180, 4)

    # Красные глаза с чёрной обводкой
    circle(screen, BLACK, (170, 210), 15)
    circle(screen, RED, (170, 210), 35, 20)

    circle(screen, BLACK, (330, 210), 15)
    circle(screen, RED, (330, 210), 35, 20)

    # Злые брови
    line(screen, BLACK, (110, 165), (210, 190), 20)
    line(screen, BLACK, (280, 190), (390, 155), 20)

    # Злой рот
    rect(screen, BLACK, (160, 310, 180, 50))

    pygame.display.flip()

pygame.quit()