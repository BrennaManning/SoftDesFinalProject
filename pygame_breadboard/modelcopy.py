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
#       self.pos = ()
        self.components = []
        self.state = 0
        self.states = ["State 0: user needs to click the component to begin placement", "State 1: user needs to click the position of the component"]

    def update(self):
        """updates all aspects of the game"""
        events = pygame.event.get()
        self.run()

    def run(self):
        while True:
            Background.get_drawables
            self.update_components() 

    def update_components(self):
        """ updates all aspects of the game """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos() 
                if self.state == 0:
                    self.mpos1 = mpos
                    self.mpos2 = (0,0)
                    # Component.define_type(Component(self.mpos1, self.mpos2),mpos)
                    # Component.define_value(Component(self.mpos1, self.mpos2),mpos)
                    if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
                        self.state = 1
                    print(self.states[self.state])
                else: #self.state == 1
                    #print self.selected
                    # print(self.states[self.state])

                    if mpos[0] > 200:
                        if self.state == 1:
                            self.mpos2 = mpos
                            # Component(self.mpos1,self.mpos2).define_spot(mpos)
                            # self.model_get_components(self.mpos1, self.mpos2)

                            # print(self.states[self.state])
                            self.state = 0
                            print(self.states[self.state])
                            list_of_comp_values = [self.define_type(self.mpos1),
                                self.define_value(self.mpos1),self.define_spot(self.mpos2)]
                            self.components.append(Component(list_of_comp_values))

                #print(self.states[self.state])
    def define_type(self, mpos):
        """determines what type of component is selected"""

        self.selected = "none"
        if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
            if mpos[1] < 225 and mpos[1] > 180:
                self.selected = "r1"
                self.value = "r1 value"
            elif mpos[1] < 270 and mpos[1] >225:
                self.selected = "r2"
                self.value = "r2 value"
            elif mpos[1] < 315 and mpos[1] > 270:
                self.selected = "c1"
                self.value = "c1 value"
            elif mpos[1] < 360 and mpos[1] > 315:
                self.selected = "c2"
                self.value = "c2 value"
            
            if self.selected == 'r1' or self.selected == 'r2':
                component_type = "R" 
            if self.selected == 'c1' or self.selected == 'c2':
                component_type = "C" 
            #print component_type
            
            return component_type

    def define_value(self, mpos):
        """determines what type of component is selected"""
        if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
            if mpos[1] < 225 and mpos[1] > 180:
                self.value = "r1 value"
            elif mpos[1] < 270 and mpos[1] >225:
                self.value = "r2 value"
            elif mpos[1] < 315 and mpos[1] > 270:
                self.value = "c1 value"
            elif mpos[1] < 360 and mpos[1] > 315:
                self.value = "c2 value"
            
            component_value = self.value
            #print component_value
            modelcopy.state = 1
            return component_value

    def define_spot(self,mpos):
        """ determines which specific spot had been clicked """
        mpos_coord = ((mpos[0] - 217)/95, (mpos[1] - 127)/95)
       # print mpos_coord
        if mpos_coord == (1,0) or mpos_coord == (2,0):
            spot = "1"
            #print spot
            return spot
        if mpos_coord == (3,1) or mpos_coord == (3,2):
            spot = "2"           
           #print spot
            return spot
    
    def end_program(self):
    	"""ends the program"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    	

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()

    def model_get_components(self,mpos1,mpos2):
        """forms list of components in model class"""
        print "HELLOOO???"

        model_component = Component(mpos1,mpos2).get_component
        #print model_component
        if model_component[2] != None:
            components.append[component]
        #print model_components


    def calculate_cutoff_frequencyLP(self):
        """calculates cut-off frequency of a passive low-pass filter"""
        """FOR LEVEL ONE"""
        pass

class Background(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((400,200))
        self.state = 0
        self.states = ["State 0: user needs to click the component to begin placement", "State 1: user needs to click the position of the component"]
        self.pos = (0,0)
        self.image = pygame.image.load('images/CircuitSimLevel1Background.png')
        self.image = pygame.transform.scale(self.image, (960,480))
        self.image.set_colorkey((255,255,255))
        self.selected = "none"

    def get_drawables(self):
        """Gets the drawables for the background"""
        return DrawableSurface(self.image,pygame.Rect((0,0), self.image.get_size()))

class Component():
    def __init__(self, compList):
        """initializes a component"""
        self.component_type = compList[0]
        self.component_spot = compList[2]
        self.component_value = compList[1]
        self.draw_block()
        #self.mpos2 = mpos2
        #self.spot = self.define_spot(self.mpos2)

        if self.component_type == 'R':
            self.image = pygame.image.load('images/Resistor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))
        if self.component_type == 'C':
            self.image = pygame.image.load('images/Capacitor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))

    def draw_block(self):
        """gets the drawables for the component block"""
        return DrawableSurface(self.image,pygame.Rect((self.pos),
                                self.image.get_size()))

        # self.component = self.get_component()

    # def define_type(self, mpos):
    #     """determines what type of component is selected"""

    #     self.selected = "none"
    #     if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
    #         if mpos[1] < 225 and mpos[1] > 180:
    #             self.selected = "r1"
    #             self.value = "r1 value"
    #         elif mpos[1] < 270 and mpos[1] >225:
    #             self.selected = "r2"
    #             self.value = "r2 value"
    #         elif mpos[1] < 315 and mpos[1] > 270:
    #             self.selected = "c1"
    #             self.value = "c1 value"
    #         elif mpos[1] < 360 and mpos[1] > 315:
    #             self.selected = "c2"
    #             self.value = "c2 value"
            
    #         if self.selected == 'r1' or self.selected == 'r2':
    #             component_type = "R" 
    #         if self.selected == 'c1' or self.selected == 'c2':
    #             component_type = "C" 
    #         #print component_type
            
    #         return component_type

    # def define_value(self, mpos):
    #     """determines what type of component is selected"""
    #     if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
    #         if mpos[1] < 225 and mpos[1] > 180:
    #             self.value = "r1 value"
    #         elif mpos[1] < 270 and mpos[1] >225:
    #             self.value = "r2 value"
    #         elif mpos[1] < 315 and mpos[1] > 270:
    #             self.value = "c1 value"
    #         elif mpos[1] < 360 and mpos[1] > 315:
    #             self.value = "c2 value"
            
    #         component_value = self.value
    #         #print component_value
    #         modelcopy.state = 1
    #         return component_value

    # def define_spot(self,mpos):
    #     """ determines which specific spot had been clicked """
    #     mpos_coord = ((mpos[0] - 217)/95, (mpos[1] - 127)/95)
    #    # print mpos_coord
    #     if mpos_coord == (1,0) or mpos_coord == (2,0):
    #         spot = "1"
    #         #print spot
    #         return spot
    #     if mpos_coord == (3,1) or mpos_coord == (3,2):
    #         spot = "2"           
    #        #print spot
    #         return spot


    def get_component(self):
        """ makes a list to represent the component"""
        component = []
        component = [self.component_type, self.component_value, self.spot]

        if component[2] != None:
            print component
        return component 
