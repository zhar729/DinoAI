import os 
import sys
import neat
import pygame
pygame.init()
pygame.font.init()

GRAVITY = 9.81

WIN_HEIGHT = 500
WIN_WIDTH = 800



class Dino:
    
    def __init__(self, x, y):
        pass


class Cactus:
    
    def __init(self, x):
        pass



pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

def draw_window():
    pygame.display.update()



running = True
while running:
    draw_window()

    # quit game if x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break