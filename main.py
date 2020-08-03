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


    X = 200
    WIDTH = 30
    HEIGHT = 100
    
    def __init__(self):
        self.x = 200
        self.y = 300

        self.width = 30
        self.height = 100
        
        self.y1 = self.y
        self.tick_count = 0
        self.vel = 0
        


    def draw(self):
        '''
        draws a rectangle representing the player
        :return: None
        '''
        pygame.draw.rect(win, COLOUR ,(self.x, self.y, self.width, self.height))


    def jump(self):
        '''
        jumps the dino 
        :return: None
        '''
        self.vel = -10.5
        self.tick_count = 0
        # change height
        self.y1 = self.y


    def move(self):
        '''
        updates the dino's position if it has jumped
        :return: None
        '''
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2

        if d < 0:
            d -= 2

        
        self.y = self.y + d
        if self.y >= 300:
            self.y = 300


        
        


class Cactus:
    '''
    represents the obstacles that the dino has to jump over
    '''
    pass



def draw_window(win, dino):
    '''
    draws all of the objects to the window
    :return: None
    '''

    win.fill((255, 255, 255))

    # draw base
    pygame.draw.rect(win, COLOUR ,(0, 400, 1000, 5))
    dino.draw()

    pygame.display.update()






def eval_genomes():

    dino = Dino()

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        keys = pygame.key.get_pressed()

        dino.move()
        if keys[pygame.K_SPACE]:
            dino.jump()
            
        
        draw_window(win, dino)
        time.sleep(0.05)
    
        



eval_genomes()