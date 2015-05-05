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
from view3 import *
import modelcopy3
import controller3

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
        self.game_model3 = modelcopy3.Model3(960, 480)
        self.view3 = View3(self.game_model3, 960, 480)
        self.controller3 = controller3.Controller(self.game_model3)
        self.level = 1

    def run(self):
        """ the main runloop """
        quit = False
        while not quit:
            events = pygame.event.get()
            if self.level == 1:
                self.view1.draw()
                self.controller1.process_events(events)
                self.game_model1.update(events)
                pygame.display.update()
                self.level = self.controller1.level
                quit = self.game_model1.end_program(events)
                
            elif self.level == 2:
                self.view2.draw()
                self.controller2.process_events(events)
                self.game_model2.update(events)
                pygame.display.update()
                self.level = self.controller2.level
                quit = self.game_model2.end_program(events)

            elif self.level == 3:
                self.view3.draw()
                self.controller3.process_events(events)
                self.game_model3.update(events)
                pygame.display.update()
                self.level = self.controller3.level
                quit = self.game_model3.end_program(events)
            
if __name__ == '__main__':
    board = pygameBreadboard()
    board.run()