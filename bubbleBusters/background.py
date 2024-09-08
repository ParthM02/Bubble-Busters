#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 00:53:40 2023

@author: parthmehta
"""

#Imports pygame library
import pygame
import random

#class for background objects
class Background():
    #Initialize method
    def __init__(self, pos):
        #Creates lake background
        self.num = (random.randint(1, 4))
        if self.num == 1:
            self.image = pygame.image.load('lake.png')
        #Creates petosky background
        elif self.num == 2:
            self.image = pygame.image.load('pet.png')
        #Creates palm-something background
        elif self.num == 3:
            self.image = pygame.image.load('palm.png')
        #Fall time background
        elif self.num == 4:
            self.image = pygame.image.load("fall.png")
        #Antelope Canyon background - Disabled due to coin text missing
        elif self.num == 5:
            self.image = pygame.image.load("antelope.png")
        #Denali Background - Disabled due to coin text missing in antelope Canyon
        elif self.num == 6:
            self.image = pygame.image.load("denali.png")
        #self.image = image
        #Gets x position for the bubble
        self.x_pos = pos[0]
        #Gets y position for the bubble
        self.y_pos = pos[1]
        #Redundancy for lack of image
        if self.image is None:
            self.image = self.text
        #Creates boundary for bubble
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		#self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    #Displays background object
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
		#screen.blit(self.text, self.text_rect)

    #Checks if background is pressed
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    #Changes color of background - not referenced too lazy to delete cuz scared it is referenced
    def changeColor(self):
        self.num = (random.randint(1, 3))
        if self.num == 1:
            self.image = pygame.image.load('blueBub.png')
        #Creates green bubble
        elif self.num == 2:
            self.image = pygame.image.load('greenBub.png')
        #Creates red bubble
        elif self.num == 3:
            self.image = pygame.image.load('redBub.png')
        #self.image = pygame.image.load('greyBub.png')