"""make breadboard. wire circuits. pass iSIM"""

import random
from random import randint
import time
import pygame
from modelcopy import Model
from view import *
from controller import *


class pygameBreadboard():
    """ The main class """
    def __init__(self):
        """ Initialize the board """
        self.game_model1 = Model(960, 480)
        self.view1 = View(self.game_model1, 960, 480)
        self.controller1 = Controller(self.game_model1)
        self.level = 1
    def run(self):
        """ the main runloop """
        self.level = 1
        if self.level == 1:
            while not(self.game_model1.end_program()):
                self.view1.draw()
                self.controller1.process_events()
                self.game_model1.update()
                pygame.display.update()
    

if __name__ == '__main__':
    board = pygameBreadboard()
    board.run()