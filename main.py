import os 
import sys
import neat
import pygame
import time
pygame.init()
pygame.font.init()

GRAVITY = 9.81

COLOUR = (0, 0, 0)

WIN_HEIGHT = 500
WIN_WIDTH = 800

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))



class Dino:
    X_POS = 0
    WIDTH = 0
    HEIGHT = 0
    
    def __init__(self, y):
        self.y_pos = y


class Cactus:
    Y_POS = 400
    
    def __init__(self, x):
        self.x = x


class Base:
    X_POS = 0
    Y_POS = 400
    WIDTH = 1000
    HEIGHT = 5
    

    def __init__(self):
        self.drawn = False


    def draw(self):
        '''
        draw the base to the screen
        '''
         
        pygame.draw.rect(win, COLOUR ,(self.X_POS ,self.Y_POS  ,self.WIDTH ,self.HEIGHT))





base = Base()

def draw_window(win, base):

    win.fill((255, 255, 255))
    base.draw()

    pygame.display.update()



def update():
    draw_window(win, base)

    time.sleep(0.05)



running = True
while running:
    
    update()

    # quit game if x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break