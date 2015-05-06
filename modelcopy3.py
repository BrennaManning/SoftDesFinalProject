import random
from random import randint
import time
import pygame
from view import *
from controller import *
from math import pi

class Model3():
    """ Represents the game state of the scroller """
    def __init__(self, width, height):
        """ Initialize the model """
        self.width = width
        self.height = height
        self.background = Background()
        self.component_list = []
        self.r1 = 0
        self.c1 = 0
        self.r2 = 0
        self.c2 = 0
        self.cutoff_freql_text = "?"
        self.cutoff_freqh_text = "?"
        self.cutoff_freql = 0
        self.cutoff_freqh = 0
        self.drawables = []
        self.voltage = "?"

    def update(self, events):
        """updates all aspects of the game"""
        events = events
         
    def calculate_bandwidth(self, complist):    
        """calculates the cutoff frequency for a low pass filter"""

        self.type = complist[0]
        self.spot = complist[2]
        self.value = complist[1]
        self.fail = False

        if self.spot == "1" or self.spot == "2":
            # print "Calculation if Loop 1st filter"
            if self.type == "C":
                if self.c1 == 0:
                    self.c1 = self.value
                else:
                    self.fail = True
            else:
                if self.r1 == 0:
                    self.r1 = self.value
                else:
                    self.fail = True

        if self.spot == "3" or self.spot == "4":
            # print "Calculation if loop 2nd filter"
            if self.type == "C":
                if self.c2 == 0:
                    self.c2 = self.value
                else:
                    self.fail = True
            else: #self.type == "R"
                if self.r2 == 0:
                    self.r2 = self.value
                else:
                    self.fail = True

        if self.c1 != 0 and self.c2 != 0 and self.r1 != 0 and self.r2 != 0:
            cf_low = int((1/(2*pi*(self.r1)*(self.c1))/1000))
            #print "hello!"
            cf_low = str(cf_low)
            self.cutoff_freql = cf_low
            self.cutoff_freql_text = cf_low + "K"
            print self.cutoff_freql_text
            cf_high = int((1/(2*pi*(self.r2)*(self.c2))/1000))
            cf_high = str(cf_high)
            self.cutoff_freqh = cf_high
            self.cutoff_freqh_text = cf_high + "K"
            print self.cutoff_freqh_text
            voltage_change = float((self.r2)/self.r1)
            voltage = 5 + voltage_change
            self.voltage = str(voltage)
            print self.voltage

    def define_type(self, mpos):
        """determines what type of component is selected"""

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
            if self.selected == 'r1' or self.selected == 'r2':
                component_type = "R" 
            if self.selected == 'c1' or self.selected == 'c2':
                component_type = "C"
            return component_type

    def define_value(self, mpos):
        """determines what type of component is selected"""
        if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
            if mpos[1] < 225 and mpos[1] > 180:
                self.value = 3390 #3.39k ohm
            elif mpos[1] < 270 and mpos[1] >225:
                self.value = 16900 #16.9 k ohm
            elif mpos[1] < 315 and mpos[1] > 270:
                self.value = float(0.00000000047)
            elif mpos[1] < 360 and mpos[1] > 315:
                self.value = float(0.000000000047)
            
            component_value = self.value
            return component_value

    def define_spot(self,mpos):
        """ determines which specific spot had been clicked """
        mpos_coord = ((mpos[0] - 199)/87, (mpos[1] - 116)/87)
        if mpos_coord == (1,2):
            spot = "1"
            return spot
        if mpos_coord == (2,2):
            spot = "2"           
            return spot
        if mpos_coord == (4,0):
            spot = "3"
            return spot
        if mpos_coord == (4,1):
            spot = "4"           
            return spot
        else:
            return False
    
    def end_program(self, events):
        """ends the program"""
        for event in events:
            if event.type == pygame.QUIT:
                return True

    def get_all_drawables(self):
        """ gets all drawables from various places """   
        drawables = []
        if len(self.component_list) > 0:
            for c in self.component_list:
                drawables.append(c.get_drawables())
        return drawables

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()

    def get_components_drawables(self):
        """ return a list of Drawable Surfaces for the view """
        # print self.component_list
        print len(self.component_list)
        for c in self.component_list:
            return c.get_drawables()

class DrawableSurface():
    """ A class that wraps a pygame.Surface and a pygame.Rect """
    def __init__(self, surface, rect):
        """ Initialize the drawable surface """
        self.surface = surface
        self.rect = rect

    def get_surface(self):
        """ Get the surface """
        return self.surface

    def get_rect(self):
        """ Get the rect """
        return self.rect
   
class Background(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((400,200))
        self.pos = (0,0)
        self.image = pygame.image.load('images/CircuitSimLevel3Background.png')
        self.image = pygame.transform.scale(self.image, (960,480))
        self.image.set_colorkey((255,255,255))
        self.selected = "none"

    def get_drawables(self):
        """Gets the drawables for the background"""
        return DrawableSurface(self.image,pygame.Rect((0,0), self.image.get_size()))

class Component():
    def __init__(self, compList):
        """initializes a component"""
        self.component_value = compList[1]
        self.component_spot = compList[2]
        self.image = self.component_type(self.component_spot, compList[0])

    def get_drawables(self):
        """ gets a list of all enemy drawables"""
        return DrawableSurface(self.image, pygame.Rect(
                                        (self.spot_coords(self.component_spot)),
                                        self.image.get_size()))

    def component_type(self, spot, comptype):
        """ determines the component type based on the input """
        if comptype == 'R':
            self.image = pygame.image.load('images/Resistor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))
        elif comptype == 'C':
            self.image = pygame.image.load('images/Capacitor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))
        return self.image

    def spot_coords(self,spot):
        """ given a designated spot, returns the necessary x,y values """
        if spot == '1':
            return (330 - 60 ,335 - 15)
        if spot == '2':
            return (419 - 60, 335 - 15)
        if spot == '3':
            return (591 - 60, 159 - 15)
        if spot == '4':
            return (588 - 60, 248 - 15)

    def draw_block(self):
        """gets the drawables for the component block"""
        draw_component = DrawComponent(self.component_spot,self.component_type)
        return draw_component

    def get_component(self):
        """ makes a list to represent the component"""
        component = []
        component = [self.component_type, self.component_value, self.spot]

        if component[2] != None:
            print component
        return component