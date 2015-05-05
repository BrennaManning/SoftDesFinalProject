import random
from random import randint
import time
import pygame
import modelcopy3

class Controller():
    def __init__(self, model):
        """ the control class """
        self.game_model = model
        self.state = 0
        self.states = ["State 0: user needs to click the component to begin placement", 
                       "State 1: user needs to click the position of the component",
                       "you won!"]
        self.level = 3

    def process_events(self, events):
        """ process keyboard events. Function called periodically """
        g = self.game_model
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
                    self.mpos2 = mpos
                    if g.define_spot(self.mpos2) != False:
                        self.list_of_comp_values = [g.define_type(self.mpos1),
                                                    g.define_value(self.mpos1),
                                                    g.define_spot(self.mpos2)]                            
                        g.calculate_bandwidth(self.list_of_comp_values)
                        g.component_list.append(modelcopy3.Component(self.list_of_comp_values))
                        if len(g.component_list) > 3:
                            if int(g.cutoff_freql) > 98:
                                if int(g.cutoff_freqh) > 199:
                                    self.state = 2
                            else:
                                g.component_list = []
                                self.state = 0
                                print "Not quite right, try again"
                                print "hint: cutoff = 1/(2pi*R1*C1)"
                        else:
                            self.state = 0
                        print(self.states[self.state])
                elif self.state == 2:
                #STATE: NEXT LEVEL
                    print "GAME WON -- FOR NOW"
                    print "...>>>>>....>>>>>....."
                    print "brought to you by!!!"
                    print "MICHAEL AND BRENNAAAAAAA"