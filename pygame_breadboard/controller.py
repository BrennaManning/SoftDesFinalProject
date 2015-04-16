import random
from random import randint
import time
import pygame


class Controller():
    def __init__(self, model):
	""" the control class """
    	self.model = model
        self.state = 0

    def process_events(self):
        """ process keyboard events. Function called periodically """
        pygame.event.pump()
        
        # if pygame.event.type == pygame.MOUSEBUTTONDOWN:
            # pass

            # mpos = pygame.mouse.get_pos()
                # if self.state = 0:

        if pygame.mouse.get_pressed() != (1, 0, 0):
            self.mouse_pressed = False
        elif not (self.mouse_pressed):
            self.mouse_pressed = True
            mpos = pygame.mouse.get_pos()
            if mpos[0] >= 75 and mpos[0] <= 250:
                if mpos[1] >= 115 and mpos[1] <= 150:
                    pass