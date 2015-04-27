import random
from random import randint
import time
import pygame
import modelcopy
from controller import *

class View():
    def __init__(self, g_model, width, height):
        """ Initialize the view. The input model is necessary to find 
            the position of relevant objects to draw. """
        pygame.init()
        #determine where to draw
        self.screen = pygame.display.set_mode((width, height))
        self.game_model = g_model
             
        #self.game_model = model.Model(960, 480)
        #self.view = View(self.game_model, 960, 480)
        #self.controller = Controller(self.game_model)
        pygame.font.init()
        self.myfont = pygame.font.SysFont("monospace", 15)
        self.V_text = "?"
      
        self.cutoff_frequency_text = self.game_model.cutoff_frequency_text

    def draw(self):
        """ Redraw the full game window """
        # get the new drawables
        d = self.game_model.get_background_drawables()
        rect = d.get_rect()
        surf = d.get_surface()
        surf.set_colorkey((255,255,255))
        self.screen.blit(surf, rect)
        self.r1_button = pygame.image.load('images/Resistor.png')
        self.r1_button = pygame.transform.scale(self.r1_button, (120, 30))
        self.screen.blit(self.r1_button,(60,180))
        r1_label = self.myfont.render("100k ohm R", 1, (0,0,0))
        self.screen.blit(r1_label, (70, 215))
        self.r2_button = pygame.image.load('images/Resistor.png')
        self.r2_button = pygame.transform.scale(self.r2_button, (120, 30))
        self.screen.blit(self.r2_button,(60,230))
        r2_label = self.myfont.render("1k ohm R", 1, (0,0,0))
        self.screen.blit(r2_label, (70, 265))
        self.c1_button = pygame.image.load('images/Capacitor.png')
        self.c1_button = pygame.transform.scale(self.c1_button, (120, 30))
        self.screen.blit(self.c1_button, (60,280))
        c1_label = self.myfont.render("2.6 uF C", 1, (0,0,0))
        self.screen.blit(c1_label, (70, 315))
        self.c2_button = pygame.image.load('images/Capacitor.png')
        self.c2_button = pygame.transform.scale(self.c2_button, (120, 30))
        self.screen.blit(self.c2_button, (60,330))
        c2_label = self.myfont.render("10 uF C", 1, (0,0,0))
        self.screen.blit(c2_label, (70, 365))
       
        COF_Text = self.myfont.render(self.cutoff_frequency_text, 1, (0,0,0))
        self.screen.blit(COF_Text, (855, 302))
        V_Text = self.myfont.render(self.V_text, 1, (0,0,0))
        self.screen.blit(V_Text, (855, 192))

       


class DrawComponent():
    """A class that draws components in position"""
    def __init__(self,spot,ctype):
        """initializes the class"""
        self.spot = spot
        self.component_type = ctype

        if self.component_type == "R":
            self.image = pygame.image.load('images/Resistor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))
        if self.component_type == "C":
            self.image = pygame.image.load('images/Capacitor.png')
            self.image = pygame.transform.scale(self.image, (120, 30))

        if self.spot == "1":
            self.pos = (500, 200)

        if self.spot == "2":

            self.pos = (700, 300)

        return DrawableSurface(self.image,pygame.Rect((self.pos),
                                self.image.get_size()))


        pass

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
