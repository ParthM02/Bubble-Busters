#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:38:54 2023

@author: parthmehta
"""

import pygame

#Power-up object class
class PowRoc():
    #Initialize method
    def __init__(self, pos, type):
        #Sets image to horizontal rocket I think, could be vertical
        if type == 1:
            self.image = pygame.image.load("rocket.png")
        #Sets image to vertical rocket I think, could be horizontal
        elif type == 2:
            self.image = pygame.image.load("rocket2.png")
        #Sets image to explosion
        elif type == 3:
            self.image = pygame.image.load("explosion.png")
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
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            screen.blit(self.image, self.rect)
		#screen.blit(self.text, self.text_rect)

    