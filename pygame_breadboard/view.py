import random
from random import randint
import time
import pygame
import model
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
        self.r2_button = pygame.image.load('images/Resistor.png')
        self.r2_button = pygame.transform.scale(self.r2_button, (120, 30))
        self.screen.blit(self.r2_button,(60,230))
        self.c1_button = pygame.image.load('images/Capacitor.png')
        self.c1_button = pygame.transform.scale(self.c1_button, (120, 30))
        self.screen.blit(self.c1_button, (60,280))
        self.c2_button = pygame.image.load('images/Capacitor.png')
        self.c2_button = pygame.transform.scale(self.c2_button, (120, 30))
        self.screen.blit(self.c2_button, (60,330))

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
