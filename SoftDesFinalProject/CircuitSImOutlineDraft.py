"""OUTLINE


Model:

	Nodes
	Connections
	

View:

	Pygame Window 
	Update when user put object in place
	Capacitor or resistor object to between nodes clicked

Controller:

	User clicks
	Nodes correspond to coordinates on pygame view window
	Depending what noedes are clicked and whether it is a click1 or a click 2
	->Manipulates Model

Click 1 
Click 2


Nodes have connections
"""



"""VIEW"""



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

class Connect


#Model stuff
"""MODEL"""


class Model():
    """ Represents the game state """
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
    	events = pygame.quit

    def get_background_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables()

    def add_node(self):
    	""" adds a node to the list of nodes, to be used in voltage and 
    		current calculations"""
		self.nodes.append(add_node)



connection_list = []
#node list = [(list of nodes)]

while Click == True: 
	click1 == True
	if click1 == True:
		node = click.node
		clicklocation1 = node.position
		##Something like this here
		#Find the node from the node list 

		for node in range(len(nodelist)):
			if node.connections > 2:
				#it is NOT in series
				#Different Rules
			else: #it is in series
				Connection[node(i)] =  “node(i)” + “node(i+1)”
				connection_list.append(Connection[node(i)])

		click1 == False
		click2 == True
	elif click2 == True:
		node = click.node
		clicklocation2 = node.position
		#Not this exactly but something here to get the node that was clicked from node_list

		#pygame draw line (clicklocation1 to clicklocation2)


### ETC ETC



"""CONTROLLER"""

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



