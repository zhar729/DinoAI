import os 
import sys
import neat
import pygame
import time
pygame.init()
pygame.font.init()

GRAVITY = 9.81

COLOUR = (100, 100, 100)

WIN_HEIGHT = 500
WIN_WIDTH = 800

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Chrome dino game')



class Dino:
    '''
    represents the player
    '''


    X_POS = 200
    WIDTH = 30
    HEIGHT = 100
    
    def __init__(self):
        self.y_pos = 300



        self.jumping = False
        self.jump_count = 0


    def draw(self):
        '''
        draws a rectangle representing the player
        :return: None
        '''
        pygame.draw.rect(win, COLOUR ,(self.X_POS, self.y_pos, self.WIDTH, self.HEIGHT))


    def jump(self):
        '''
        increase upward vel when jump button is pressed
        :return: None
        '''
        pass


    
    def move(self):
        '''
        updates upward vel
        :return: None
        '''
        pass


class Cactus:
    '''
    represents the obstacles that the dino has to jump over
    '''
    pass


class Base:
    '''
    represents the base
    '''

    X_POS = 0
    Y_POS = 400
    WIDTH = 1000
    HEIGHT = 5
    

    def __init__(self):
        self.drawn = False


    def draw(self):
        '''
        draw the base to the screen
        :return: None
        '''
         
        pygame.draw.rect(win, COLOUR ,(self.X_POS, self.Y_POS, self.WIDTH, self.HEIGHT))







def draw_window(win, base, dino):
    '''
    draws all of the objects to the window
    :return: None
    '''

    win.fill((255, 255, 255))
    base.draw()
    dino.draw()

    pygame.display.update()






def eval_genomes():

    base = Base()
    dino = Dino()

    def update():
        '''
        called every frame
        :return: None
        '''

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            dino.jump()

        dino.move()
    
        draw_window(win, base, dino)
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


eval_genomes()