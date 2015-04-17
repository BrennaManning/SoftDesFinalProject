# http://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect
# find out how someone made a collidepoint button
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
        self.image = pygame.image.load('images/CircuitSimLevel1Background.png')
        #small nitpicky point here that others may or may not agree on depending on what conventions they use: you guys save your variables to self.somethin and then perform operations on the something. Often when I see self.something, I expect to see the value being set and not being modified right away. just use a normal variable, perform operations on it, and then set self.something to what you need it to be.
        # self.image = pygame.image.load('images/breadboard_background.jpg')
        self.image = pygame.transform.scale(self.image, (960,480))
        self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        """ Gets the drawables for the background """
        return DrawableSurface(self.image,
                                pygame.Rect((0,0), self.image.get_size()))

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
#given what the function does, I'd rename this function to get_drawables as well. 
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

class Blocks():
    pass


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
        #are there more informative names than pos(1,2,3) that you could use?
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

    def update(self):
        """ updates all aspects of the game """
        events = pygame.event.get()
        pygame.event.pump
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.mouse_pressed = True
            self.resistor.pos = pygame.mouse.get_pos()
            self.resistor.draw_block

    def end_program(self):
    	"""ends the program"""
    	pass

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()


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
        rect = d.get_rect()
        surf = d.get_surface()
        surf.set_colorkey((255,255,255))
        self.screen.blit(surf, rect)
#another thing to think about is that once you get to user input adding resistors or capacitors, it should look a little something like this: user clicks, so controller edits the model to have a Resistor object where the user clicked. The view, in turn, gets_drawables from the Model class, which returns a list of drawables, and that list includes the newly added resistor object's drawables. Then the view draws the drawables.
        self.r1_button = pygame.image.load('images/Resistor.png')
        self.r1_button = pygame.transform.scale(self.r1_button, (120, 30))
        self.screen.blit(self.r1_button,(60,180))
        self.r2_button = pygame.image.load('images/Resistor.png')
        self.r2_button = pygame.transform.scale(self.r2_button, (120, 30))
        self.screen.blit(self.r2_button,(60,230))
        self.c1_button = pygame.image.load('images/Capacitor.png')
        self.c1_button = pygame.transform.scale(self.c1_button, (120, 30))
        self.screen.blit(self.c1_button, (60,280))
        self.c2_button = pygame.image.load('images/Capacitor.png')
        self.c2_button = pygame.transform.scale(self.c2_button, (120, 30))
        self.screen.blit(self.c2_button, (60,330))
#hm, it seems like this part of the GUI that your building (if I understand correctly) will stay the same through the levels. Ya'll should consider just putting everything into one image so you don't have to separately load them and specify where they're drawn, if that's the case. Could everything (background and nonchanging gui elements) be considered one background that you load?

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

class pygameBreadboard():
    """ The main class """
    def __init__(self):
        """ Initialize the board """
        self.game_model = Model(960, 480)
        self.view = View(self.game_model, 960, 480)
        self.controller = Controller(self.game_model)

    def run(self):
        """ the main runloop """
        while not(self.game_model.end_program()):
            self.view.draw()
            self.controller.process_events()
            #To utilize MVC well, use the controller to update the model! Think of the model as a store of data that gets changed by the user input (the controller). Model update stuff should be stuff that happens without user input, like a ball in brick breaker continuing to move in the direction that it's going, for instance. There seems to be a bit of a misunderstanding here about how the controller is meant to be used. Feel free to ask me more.
            self.game_model.update()
            pygame.display.update()


if __name__ == '__main__':
    board = pygameBreadboard()
    board.run()
