import random
from random import randint
import time
import pygame
import modelcopy
import modelcopy2
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

    def process_events(self, events):

        """ process keyboard events. Function called periodically """
        pygame.event.pump()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos() 
                #Gets mouse position
                if self.state == 0:
                    #STATE: SELECT COMPONENT
                    self.mpos1 = mpos
                    self.mpos2 = (0,0)
                    if mpos[0] > 60 and mpos[0] < 180 and mpos[1] > 180 and mpos [1] < 360:
                        self.state = 1
                    print(self.states[self.state])
                elif self.state == 1:
                    #STATE: PLACE COMPONENT
                    if mpos[0] > 200:
                        if self.state == 1:
                            self.mpos2 = mpos

                            print(self.states[self.state])
                            self.list_of_comp_values = [self.game_model.define_type(self.mpos1),
                                self.game_model.define_value(self.mpos1),
                                self.game_model.define_spot(self.mpos2)]
                            

                            #self.view.cutoff_frequency_text = self.game_model.cutoff_frequency_text
                            #print self.view.cutoff_frequency_text 
                            
                            print self.list_of_comp_values
                            self.game_model.calculate_LP_cutoff(self.list_of_comp_values)
                            self.game_model.component_list.append(modelcopy.Component(self.list_of_comp_values))
                           # self.game_model.components.append(modelcopy.Component(self.list_of_comp_values).get_component)
                            if len(self.game_model.component_list) > 1:
                                self.state = 2
                            else:
                                self.state = 0

                elif self.state == 2:
                    self.level = 2


                           # if self.game_model.cutoff_frequency_text == "61":
                            #    pygame.time.wait(5000)
                            # self.level = 2


