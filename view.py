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
        self.screen = pygame.display.set_mode((width, height))
        self.game_model = g_model
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
       
        COF_Text = self.myfont.render(self.game_model.cutoff_frequency_text, 1, (0,0,0))   
        self.screen.blit(COF_Text, (855, 302))
        if COF_Text != "?":
            self.V_text =  "5"
        V_Text = self.myfont.render(self.V_text, 1, (0,0,0))
        self.screen.blit(V_Text, (855, 192))

        drawables = self.game_model.get_all_drawables() 
        for d in drawables:
            rect = d.get_rect()
            surf = d.get_surface()
            surf.set_colorkey((255,255,255))
            self.screen.blit(surf, rect)

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
