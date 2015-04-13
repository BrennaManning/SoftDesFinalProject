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
        self.image = pygame.image.load('images/circuitsim.png')
        self.image = pygame.transform.scale(self.image, (720,360))
        self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        """ Gets the drawables for the background """
        return DrawableSurface(self.image,
                                pygame.Rect((0,0), self.image.get_size()))

# class Nodes():
#     """ represents all indicated places for circuit connectors """
#     def __init__(self, pos_x, pos_y):
#     	pass

#     def update(self):
#         """ updates current and voltage values of nodes"""
#         pygame.event.pump()

# 	def calculate_voltage(self,model):

# 	def calculate_current(self,model):

class Resistor():
    pass

class Capacitor():
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

# class Connections():
# 	""" represents all placed connections, including wires, resistors, and 
# 		capacitors """
# 	def __init___(self, node_1, node_2, type, value):
# 		pass

# 	def get_drawables():
# 		""" draws the circuit components on the breadboard """

class Model():
    """ Represents the game state of the scroller """
    def __init__(self, width, height):
        """ Initialize the model """
        self.width = width
        self.height = height
        self.background = Background()
        self.nodes = []
        self.connections = []

    def update(self):
        """ updates all aspects of the game """
        events = pygame.event.get()

    def end_program(self):
    	"""ends the program"""
    	pass

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()

    # def add_node(self,mpos):
    # 	""" adds a node to the list of nodes, to be used in voltage and 
    # 		current calculations"""
    # 	self.nodes.append(Nodes(mpos[0],mpos[1]))
    # 	print len(self.nodes)

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
            return mpos
            
	def add_connection(self):
		""" processes the series of clicks required to generate connections
			outputs a list consisting of the first connection node, the second,
			the connection type (wire, R,C, etc), and the connection value """

        pass
		# connection_factors = []

		# pygame.event.pump()
		# if pygame.mouse.get_pressed() != (1, 0, 0):
	 #        self.mouse_pressed = False
		# elif not (self.mouse_pressed):
		#     self.mouse_pressed = True
		#     mpos = pygame.mouse.get_pos()
	 #        if len(connection_factors) < 2:
		# 	    mpos = ((mpos[0]-275)/70 + 1,(mpos[1]-65)/85 + 1)
  #               if mpos[0] > 0 and mpos[0] < 7:
  #                   if mpos[1] > 0 and mpos[1] < 4:
  #                       self.model.add_node(mpos)

class pygameBreadboard():
    """ The main class """
    def __init__(self):
        """ Initialize the board """
        self.game_model = Model(720, 360)
        self.view = View(self.game_model, 720, 360)
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