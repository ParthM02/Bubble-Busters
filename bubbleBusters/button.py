#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 07:57:58 2023

@author: parthmehta
"""

""", typeB"""

#Button object class
class Button():
    #Initialize method
    def __init__(self, image, pos):
        #Sets image
        self.image = image
        #Sets x position
        self.x_pos = pos[0]
        #Sets y position
        self.y_pos = pos[1]
        #Redundancy for if image doesn't exist
        if self.image is None:
            self.image = self.text
        #Creates boundary for image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		#self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    #Prints the object
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
		#screen.blit(self.text, self.text_rect)

    #Checks if object is pressed
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    #Change color function
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)