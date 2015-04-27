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

    def process_events(self):
        """ process keyboard events. Function called periodically """
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
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
                            self.view.cutoff_frequency_text = self.game_model.cutoff_frequency_text

                            print self.list_of_comp_values
                            self.game_model.calculate_LP_cutoff(self.list_of_comp_values)

                            self.game_model.components.append(modelcopy.Component(self.list_of_comp_values).get_component)
                            #print self.game_model.components
                            #for component in self.game_model.components:
                                #print modelcopy.Component(list_of_comp_values).component_value
                               
        # if pygame.event.type == pygame.MOUSEBUTTONDOWN:
            # pass
            # mpos = pygame.mouse.get_pos()
                # if self.state = 0:

        # if pygame.mouse.get_pressed() != (1, 0, 0):
        #     self.mouse_pressed = False
        # elif not (self.mouse_pressed):
        #     self.mouse_pressed = True
        #     mpos = pygame.mouse.get_pos()
        #     if mpos[0] >= 75 and mpos[0] <= 250:
        #         if mpos[1] >= 115 and mpos[1] <= 150:
        #             pass
# To utilize MVC well, use the controller to update the model! Think of the 
# model as a store of data that gets changed by the user input (the 
# controller). Model update stuff should be stuff that happens without user 
# input, like a ball in brick breaker continuing to move in the direction that
# it's going, for instance. There seems to be a bit of a misunderstanding here
# about how the controller is meant to be used. Feel free to ask me more. 