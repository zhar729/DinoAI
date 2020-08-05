import os 
import sys
import neat
import pygame
import time
import random
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
    
    def __init__(self):
        self.x = 200
        self.y = 300

        self.width = 30
        self.height = 100

        self.jump_count = 0
        self.duck_count = 0
        self.vel = 0

        self.jumping = False
        self.ducking = False
        


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
        if not self.jumping and not self.ducking:
            self.jumping = True
            self.vel = -10.5
            self.jump_count = 0



    def move(self):
        '''
        updates the dino's position if it has jumped
        :return: None
        '''
        self.jump_count += 1

        d = self.vel*self.jump_count + 1.2*self.jump_count**2

        if d < 0:
            d -= 2

        self.y = self.y + d
        if self.y >= 300:
            self.jumping = False
            self.y = 300
            self.height = 100

        
        self.duck_count += 1

        if self.ducking:
            self.height = 50
            self.y = 350

        # when the ducking has ended
        if self.duck_count >= 12 and not self.jumping:
            self.ducking = False
            self.y = 300
            self.height = 100


    def duck(self):
        '''
        allows the dino to duck under obstacles
        :return: None
        '''
        if not self.ducking and not self.jumping:
            self.ducking = True
            self.duck_count = 0
            self.height = 50
            self.y = 350
    

            

class Cactus:
    '''
    represents the obstacles that the dino has to jump over
    '''

    TYPES = ['short_cactus', 'tall_cactus', 'bird']

    def __init__(self):
        self.width = 30
        self.passed = False
        self.x = WIN_WIDTH
        self.vel = 15

        self.type = self.TYPES[random.randint(0, 2)]
        if self.type == 'short_cactus':
            self.y = 350
            self.height = 50
        if self.type == 'tall_cactus':
            self.y = 300
            self.height = 100
        if self.type == 'bird':
            self.y = 320
            self.height = 50


    def move(self):
        '''
        moves the cactus across the screen
        :return: None
        '''
        self.x -= self.vel

    def draw(self):
        '''
        draws the obstacle to the screen
        :return: None
        '''
        pygame.draw.rect(win, COLOUR ,(self.x, self.y, self.width, self.height))

        





def draw_window(win, dino, cacti):
    '''
    draws all of the objects to the window
    :return: None
    '''

    win.fill((255, 255, 255))

    # draw base
    pygame.draw.rect(win, COLOUR ,(0, 400, 1000, 5))
    dino.draw()

    for cactus in cacti:
        cactus.draw()

    pygame.display.update()



def eval_genomes():
    
    dino = Dino()
    cacti = [Cactus()]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        keys = pygame.key.get_pressed()



        dino.move()
        if keys[pygame.K_UP]:
            dino.jump()

        if keys[pygame.K_DOWN]:
            dino.duck()
            
        for cactus in cacti:
            cactus.move()

        draw_window(win, dino, cacti)
        time.sleep(0.05)
    
        



eval_genomes()