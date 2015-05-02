import random
from random import randint
import time
import pygame
import modelcopy
import view

class Controller():
    def __init__(self, model):
	""" the control class """
        #self.game_model = model.Model(960, 480)
        self.game_model = model
        self.state = 0
        self.states = ["State 0: user needs to click the component to begin placement", "State 1: user needs to click the position of the component"]
        self.view = view.View(self.game_model, 960, 480)
        self.level = 1


    def process_events(self,events):
        """ process keyboard events. Function called periodically """
        pygame.event.pump()
        for event in events:
            # if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos() 
                if self.state == 0:
                    self.mpos1 = mpos
                    self.mpos2 = (0,0)
                    if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
                        self.state = 1
                    print(self.states[self.state])
                else: #self.state == 1
                    if mpos[0] > 200:
                        if self.state == 1:
                            self.mpos2 = mpos
                            self.state = 0
                            print(self.states[self.state])
                            self.list_of_comp_values = [self.game_model.define_type(self.mpos1),
                                self.game_model.define_value(self.mpos1),
                                self.game_model.define_spot(self.mpos2)]
                            #self.view.cutoff_frequency_text = self.game_model.cutoff_frequency_text
                            #print self.view.cutoff_frequency_text 
                            
                            print self.list_of_comp_values
                            self.game_model.calculate_LP_cutoff(self.list_of_comp_values)
                            self.game_model.component_list.append(modelcopy.Component(self.list_of_comp_values))
                            
                            if self.game_model.cutoff_frequency_text == "61":
                                pygame.time.wait(5000)
                                self.level = 2