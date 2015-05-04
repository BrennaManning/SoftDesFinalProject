import random
from random import randint
import time
import pygame
from view import *
from controller import *
from math import pi

class Model2():
    """ Represents the game state of the scroller """
    def __init__(self, width, height):
        """ Initialize the model """
        self.width = width
        self.height = height
        self.background = Background()
        self.component_list = []
        self.r = 0
        self.c = 0
        self.cutoff_frequency_text = "?"
        self.level = 1
        self.drawables = []
        
    
    def update(self, events):
        """updates all aspects of the game"""
        # pass
        events = events
        Background.get_drawables
 

    def calculate_LP_cutoff(self, complist):    
        """calculates the cutoff frequency for a low pass filter"""\

        self.type = complist[0]
        self.spot = complist[2]
        self.value = complist[1]
        self.fail = False

        if self.spot == "1":
            
            if self.type == "C":
                self.c = self.value
                
            else:
                self.fail = True
            if self.fail == True:
                print "Not a lowpass filter: try again"

        elif self.spot == "2":
            
            if self.type == "R":
                
                self.r = self.value
            else:
                self.fail = True
            if self.fail:
                print "Not a lowpass filter: try again"

        if self.r == 100000 or self.r == 1000:
            if self.c == float(0.0000026) or self.c == float(0.00001):
                LP_cutoff_f = 1/(2*pi*(self.r)*(self.c))
                #self.cutoff_frequency_text = str(LP_cutoff_f)
                LP_cutoff_f = int(LP_cutoff_f)
                LP_cutoff_f = str(LP_cutoff_f)
                print "Cut-Off Frequency = "
                print LP_cutoff_f
                self.cutoff_frequency_text = LP_cutoff_f
                return LP_cutoff_f
                if LP_cutoff_f == "61":
                    pygame.time.wait(2000)
                    self.level = 2




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
            #print component_type
            
            return component_type

    def define_value(self, mpos):
        """determines what type of component is selected"""
        if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
            if mpos[1] < 225 and mpos[1] > 180:
                self.value = 100000
            elif mpos[1] < 270 and mpos[1] >225:
                self.value = 1000
            elif mpos[1] < 315 and mpos[1] > 270:
                self.value = float(0.0000026)
            elif mpos[1] < 360 and mpos[1] > 315:
                self.value = float(0.00001)
            
            component_value = self.value
            #print component_value
            modelcopy.state = 1
            return component_value

    def define_spot(self,mpos):
        """ determines which specific spot had been clicked """
        mpos_coord = ((mpos[0] - 217)/95, (mpos[1] - 127)/95)
        if mpos_coord == (1,0) or mpos_coord == (2,0):
            spot = "1"
            return spot
        if mpos_coord == (3,1) or mpos_coord == (3,2):
            spot = "2"           
            return spot
    
    def end_program(self, events):
        """ends the program"""
        for event in events:
            if event.type == pygame.QUIT:
                return True


    def model_get_components(self,mpos1,mpos2):
        """forms list of components in model class"""
        print "HELLOOO???"

        model_component = Component(mpos1,mpos2).get_component
        #print model_component
        if model_component[2] != None:
            component_list.append[component]
        #print model_components

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
        self.state = 0
        self.states = ["State 0: user needs to click the component to begin placement", "State 1: user needs to click the position of the component"]
        self.pos = (0,0)
        self.image = pygame.image.load('images/CircuitSimLevel2Background.png')
        self.image = pygame.transform.scale(self.image, (960,480))
        self.image.set_colorkey((255,255,255))
        self.selected = "none"

    def get_drawables(self):
        """Gets the drawables for the background"""
        return DrawableSurface(self.image,pygame.Rect((0,0), self.image.get_size()))

class Component():
    def __init__(self, compList):
        """initializes a component"""
        # self.component_type = compList[0]
        self.component_value = compList[1]
        self.component_spot = compList[2]
        self.image = self.component_type(self.component_spot, compList[0])
        # View.draw_component()
        
        #self.mpos2 = mpos2
        #self.spot = self.define_spot(self.mpos2)

    def get_drawables(self):
        """ gets a list of all enemy drawables"""
        # print self.spot_coords(self.component_spot)
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
        if spot == '2':
            self.image = pygame.transform.rotate(self.image, 90)
        return self.image

    def spot_coords(self,spot):
        """ given a designated spot, returns the necessary x,y values """
        if spot == '1':
            return (408 - 60 ,175 - 15)
        if spot == '2':
            return (555 - 15,310 - 60)

    def draw_block(self):
        """gets the drawables for the component block"""
        draw_component = DrawComponent(self.component_spot,self.component_type)
        return draw_component
        #return DrawableSurface(self.image,pygame.Rect((self.pos),
                                #self.image.get_size()))

    def get_component(self):
        """ makes a list to represent the component"""
        component = []
        component = [self.component_type, self.component_value, self.spot]

        if component[2] != None:
            print component
        return component 
