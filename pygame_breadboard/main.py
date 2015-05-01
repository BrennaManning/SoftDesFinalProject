"""make breadboard. wire circuits. pass iSIM"""

import random
from random import randint
import time
import pygame
import modelcopy
from view import *
from controller import *
import modelcopy2
import controller2


class pygameBreadboard():
    """ The main class """
    def __init__(self):
        """ Initialize the board """
        self.game_model1 = modelcopy.Model(960, 480)
        self.view1 = View(self.game_model1, 960, 480)
        self.controller1 = Controller(self.game_model1)
        self.game_model2 = modelcopy2.Model2(960, 480)
        self.view2 = View(self.game_model2, 960, 480)
        self.controller2 = controller2.Controller(self.game_model2)
        self.level = 1


    def run(self):
        """ the main runloop """
        
    
        while not(self.game_model1.end_program()):
            if self.level == 1:
                self.view1.draw()
                self.controller1.process_events()
                self.game_model1.update()
                pygame.display.update()
                self.level = self.controller1.level
            
                
            elif self.level == 2:
                self.view2.draw()
                self.controller2.process_events()
                self.game_model2.update()
                pygame.display.update()
                self.level = self.controller2.level

    
if __name__ == '__main__':
    board = pygameBreadboard()
    board.run()