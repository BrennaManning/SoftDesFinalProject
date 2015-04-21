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
        #self.view_update = 
        #self.nodes = []
        #self.connections = []
        self.pos = ()
        self.components = []
        

        #self.resistor = Resistor(self.pos, "r1")
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


    def run(self):
        while True:
            self.update()
            self.get_drawables



    def update(self):
       """ updates all aspects of the game """
       
       for event in pygame.event.get():
           if event.type == pygame.QUIT: sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               mpos = pygame.mouse.get_pos() 
               if self.state == 0:
                   self.selected = "none"
                   if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
                        if mpos[1] < 225 and mpos[1] > 180:
                            self.selected = "r1"
                        elif mpos[1] < 270 and mpos[1] >225:
                            self.selected = "r2"
                        elif mpos[1] < 315 and mpos[1] > 270:
                            self.selected = "c1"
                        elif mpos[1] < 360 and mpos[1] > 315:
                            self.selected = "c2"
                        print self.selected
                        self.state = 1
               else: #self.state == 1
                   #print self.selected
                   if mpos[0] > 200:
                       if self.state == 1:
                           self.pos = mpos
                           self.state = 0
                           
               print(self.states[self.state])
               

    
    def end_program(self):
    	"""ends the program"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    	

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()


    def get_components(self):
        """forms list of components"""
        components = self.components
        #component = 
        pass


    def calculate_cutoff_frequencyLP(self):
        """calculates cut-off frequency of a passive low-pass filter"""
        """FOR LEVEL ONE"""
        pass


class component():
    def __init__(self, pos, type, value):
        """initializes a component"""
        self.pos = pos
        self.type = type
        if self.type == r:
            self.image = pygame.image.load('images/Resistor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))
        if self.type == c:
            self.image = pygame.image.load('images/Capacitor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))

        print self.pos


    def draw_block(self):
        """gets the drawables for the component block"""

        return DrawableSurface(self.image,pygame.Rect((self.pos),
                                self.image.get_size()))



