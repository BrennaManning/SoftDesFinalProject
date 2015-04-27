"""make breadboard. wire circuits. pass iSIM"""

import random
from random import randint
import time
import pygame
from model import Model
from view import *
from controller import *


class pygameBreadboard():
    """ The main class """
    def __init__(self):
        """ Initialize the board """
        self.game_model = Model(960,480)
        self.view = View(self.game_model, 960, 480)
        self.controller = Controller(self.game_model)

    def run(self):
        """ the main runloop """
        last_update_time = time.time()
        while not(self.game_model.end_program()):
            self.game_model.update()
            self.view.draw()
            self.controller.process_events()
            self.game_model.update()
            last_update_time = time.time()
            pygame.display.update()


            # level =1
            # if level == 1:
            #     self.view.draw()
            #     self.controller.process_events()
            #     self.game_model.update()
            #     pygame.display.update()
            #     k = pygame.key.get_pressed()
            #     enter = k[pygame.K_RETURN]
            #     if enter:
            #         level +=1
            # if level == 2: 
            #     self.view.draw()
            #     self.controller.process_events()
            #     self.game_model.update()
            #     pygame.display.update()
            #     k = pygame.key.get_pressed()
            #     enter = k[pygame.K_RETURN]
                
if __name__ == '__main__':
    print "does this work?"
    board = pygameBreadboard()
    board.run()