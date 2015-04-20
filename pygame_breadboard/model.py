import random
from random import randint
import time
import pygame
from view import *
from controller import *

class Model():
    """ Represents the game state of the scroller """
    def __init__(self, width, height):
        """ Initialize the model """
        self.width = width
        self.height = height
        self.background = Background()
        self.nodes = []
        self.connections = []
        self.pos = ()
        self.resistor = Resistor(self.pos, "r1")
        #self.view = View(self, 960, 480)
        #self.controller = Controller(self.game_model)
        #self.controller = Controller(self)

   

           # pygame.mouse.get_pressed() == (1, 0, 0):
            #self.mouse_pressed = True
            #self.mouse_pressed = True
            #self.resistor.pos = pygame.mouse.get_pos()
            #self.resistor.draw_block

        self.state = 0
        self.states = ["State 0: user needs to click the component to begin placement", "State 1: user needs to click the position of the component"]

    def update(self):
        """updates all aspects of the game"""
        events = pygame.event.get()
        self.background.run()

    

    def end_program(self):
    	"""ends the program"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    	

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()


    def calculate_cutoff_frequency():
        pass

class Resistor():
    def __init__(self, pos, r1):
        """ initializes a resistor """
        self.pos = pos
        self.r1 = r1
        self.image = pygame.image.load('images/Resistor.png')
        self.image = pygame.transform.scale(self.image, (120, 30))
        print self.pos
       
        print r1
        
    def draw_block(self):
        """ gets the drawables for the circuit block """
        return DrawableSurface(self.image,pygame.Rect((self.pos1),
                                self.image.get_size()))

class Capacitor():
    def __init__ (self, pos1, pos2, c1):
        """initializes a capacitor"""
        self.pos1 = pos1
        self.pos2 = pos2
        self.c1 = c1
        self.image = pygame.image.load('images/Capacitor.png')
        self.image = pygame.transform.scale(self.image, (120, 30))
        print self.pos1
        print self.pos2
        print c1
        
    def draw_block(self):
        """ gets the drawables for the circuit block """
        return DrawableSurface(self.image,pygame.Rect((self.pos1),
                                self.image.get_size()))

class HP_RC_filter():
    pass

class LP_RC_filter():
    pass

class DoubleResistor():
    """ represents a double resistor. Initialized with three positions and two 
    resistor values. """
    def __init__(self, pos1, pos2, pos3, r1, r2):
        """ initializes the double resistor """
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.r1 = r1
        self.r2 = r2
        if pos1(0) == pos3(0) or pos1(1) == pos3(1):
            self.image = pygame.image.load('images/doubresist_straight')
        else:
            self.image = pygame.image.load('images/doubresist_bent')

    def draw_block(self):
        """ gets the drawables for the circuit block """
        return DrawableSurface(self.image,pygame.Rect((self.pos1),
                                self.image.get_size()))


