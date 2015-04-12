"""make breadboard. wire circuits. pass iSIM"""

import random
from random import randint
import time
import pygame


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

class Background(pygame.sprite.Sprite):
   
    """ Represents the background """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/breadboard_background.jpg')
        self.image = pygame.transform.scale(self.image, (640,360))
        self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        """ Gets the drawables for the background """
        return DrawableSurface(self.image,
                                pygame.Rect((0,0), self.image.get_size()))

class Nodes():

    """ represents all indicated places for circuit connectors """
    
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def update(self):
        """ updates current and voltage values of nodes"""
        pygame.event.pump()

    #   def calculate_voltage(self,model):

    #   def calculate_current(self,model):

    # class Connections():
    #   """ represents all placed connections, including wires, resistors, and 
    #       capacitors """

class Model():
   
    """ Represents the game state of the scroller """

    def __init__(self, width, height):
        """ Initialize the model """
        self.width = width
        self.height = height
        self.background = Background()
        self.nodes = []

    def update(self):
        """ updates all aspects of the game """
        events = pygame.event.get()

    def end_program(self):
        """ends the program"""
        pass

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()

    def add_node(self):
        """ adds a node to the list of nodes, to be used in voltage and 
            current calculations"""

    def calculate_voltage(self, node):
        """ calculate the output voltage at a given node on the breadboard """
        pass

    def calculate_resistance(self, node):
        """calculate resistance at a given node on the breadboard """
        pass

    def calculate_current(self, node):
        """calculate current at a given node on the breadboard"""
        pass

class View():
    def __init__(self, g_model, width, height):
        
        """ Initialize the view. The input model is necessary to find 
            the position of relevant objects to draw. """
        
        pygame.init()
        #determine where to draw
        self.screen = pygame.display.set_mode((width, height))
        self.game_model = g_model

    def draw(self):
        
        """ Redraw the full game window """
        # get the new drawables
        d = self.game_model.get_background_drawables()
        # for d in self.drawables:
        rect = d.get_rect()
        surf = d.get_surface()
        surf.set_colorkey((255,255,255))
        self.screen.blit(surf, rect)

class Controller():
    def __init__(self, model):
        self.model = model
        self.mouse_pressed = False

    def process_events(self):
        """ process keyboard events. Function called periodically """
        pygame.event.pump()
        if pygame.mouse.get_pressed() != (1, 0, 0):
            self.mouse_pressed = False
        elif not (self.mouse_pressed):
            self.mouse_pressed = True
            mpos = pygame.mouse.get_pos()
            mpos = ((mpos[0]-80)/80 + 1,(mpos[1]-60)/80 + 1)
            self.model.nodes.node_add(mpos)

class Controller():
    def __init__(self, model):
        self.model = model
        self.mouse_pressed = False

    def process_events(self):
        
        """ process keyboard events. Function called periodically """
        
        pygame.event.pump()
        if pygame.mouse.get_pressed() != (1, 0, 0):
            self.mouse_pressed = False
        elif not (self.mouse_pressed):
            self.mouse_pressed = True
            mpos = pygame.mouse.get_pos()
            mpos = ((mpos[0]-80)/80 + 1,(mpos[1]-60)/80 + 1)
            self.model.nodes.node_add(mpos)


class pygameBreadboard():
    
    """ The main SideScroller class """
    
    def __init__(self):
        """ Initialize the board """
        self.game_model = Model(640, 360)
        self.view = View(self.game_model, 640, 360)
        self.controller = Controller(self.game_model)


    def run(self):
    
        """ the main runloop """
    
        while not(self.game_model.end_program()):
            self.view.draw()
            self.controller.process_events()
            self.game_model.update()
            pygame.display.update()

if __name__ == '__main__':
    board = pygameBreadboard()
    board.run() 