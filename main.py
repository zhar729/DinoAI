import os 
import sys
import neat
import pygame
import time
import random
pygame.init()
pygame.font.init()

GREY = (100, 100, 100)
LIGHT_GREY = (15, 15, 15)
RED = (255, 30, 30)
GREEN = (30, 255, 30)
BLUE = (30, 30, 255)

COLOURS = [GREY, LIGHT_GREY, RED, GREEN, BLUE]

WIN_HEIGHT = 500
WIN_WIDTH = 800

FONT = pygame.font.SysFont('arial', 45)


win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('DinoAI')



class Dino:
    '''
    represents the player
    '''
    
    def __init__(self):
        self.x = 200
        self.y = 310

        self.width = 30
        self.height = 110

        self.colour = COLOURS[random.randint(0,2)]

        self.jump_count = 0
        self.duck_count = 0
        self.vel = 0

        self.jumping = False
        self.ducking = False

        self.dead = False
        self.score = 0
        

    def draw(self):
        '''
        draws a rectangle representing the player
        :return: None
        '''
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))


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
        if self.y >= 290:
            self.jumping = False
            self.y = 290
            self.height = 110

        
        self.duck_count += 1

        if self.ducking:
            self.height = 55
            self.y = 345

        # when the ducking has ended
        if self.duck_count >= 12 and not self.jumping:
            self.ducking = False
            self.y = 290
            self.height = 110


    def duck(self):
        '''
        allows the dino to duck under obstacles
        :return: None
        '''
        if not self.ducking and not self.jumping:
            self.ducking = True
            self.duck_count = 0
            self.height = 55
            self.y = 345
    

            

class Cactus:
    '''
    represents the obstacles that the dino has to jump over
    '''

    TYPES = ['short_cactus', 'tall_cactus', 'bird']

    def __init__(self):
        self.width = 30
        self.passed = False
        self.x = WIN_WIDTH
        self.vel = 20

        self.type = self.TYPES[random.randint(0, 2)]
        if self.type == 'short_cactus':
            self.y = 350
            self.height = 50
        if self.type == 'tall_cactus':
            self.y = 300
            self.height = 100
        if self.type == 'bird':
            self.y = 250
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
        pygame.draw.rect(win, GREY ,(self.x, self.y, self.width, self.height))

        


def draw_window(win, dinos, cacti):
    '''
    draws all of the objects to the window
    :return: None
    '''

    win.fill((255, 255, 255))

    for dino in dinos:
        text = FONT.render('Score: {}'.format(str(dino.score)), 1, (100, 100, 100))


    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    # draw base
    pygame.draw.rect(win, GREY ,(0, 400, 1000, 5))

    if not dino.dead:
        dino.draw()

    for cactus in cacti:
        cactus.draw()

    
    pygame.display.update()



def eval_genomes(genomes, config):

    cacti = [Cactus()]


    dinos = []
    nets = []
    ge = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        dinos.append(Dino)
        g.fitness = 0
        ge.append(g)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        
            
        if len(dinos) == 0:
            break

        add_cactus = False
        rem = []
        for cactus in cacti:

            if not cactus.passed and cactus.x < dino.x:
                    cactus.passed = True
                    add_cactus = True

            if cactus.x <= 0:
                rem.append(cactus)

            if  pygame.Rect.colliderect(pygame.Rect(dino.x, dino.y, dino.width, dino.height), 
                                        pygame.Rect(cactus.x, cactus.y, cactus.width, cactus.height)):
                dino.dead = True

            cactus.move()



        for x, dino in enumerate(dinos):
            dino.move()
            ge.[x].fitness += 0.1       

            # the value of the output neuron
            output = nets[x].activate() 


            if output[0] > 0.5 and not output[1] > 0.5:
                dino.jump()
            if output[1] > 0.5 and not output[1] > 0.5:
                dino.duck()



        if add_cactus:
            for dino in dinos:
                if not dino.dead:
                    dino.score += 1
                cacti.append(Cactus())
            

        for r in rem:
            cacti.remove(r)


        for dino in dinos
            dino.move()


        draw_window(win, dino, cacti)
        time.sleep(0.04)
    
        



eval_genomes()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    # create the population
    popul = neat.Population(config)

    
    # show progress in the terminal
    popul.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    popul.add_reporter(stats)

    # run for up to 50 gens
    winner.popul.run(eval_genomes, 50)


if __name__ == '__main__':
    # find the config-feedforward.txt file
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)


