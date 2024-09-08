#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 00:27:16 2023

@author: parthmehta
"""

#Literal Pain - Give me a 100

#Imports pygame library
import pygame
import random

#class for bubble objects
class Bubble(pygame.sprite.Sprite):
    #Initialize method
    def __init__(self, num, pos):
        super().__init__()
        #Pause animation initially
        self.pop_animation = False
        #Array of frames for current bubble
        self.sprites = []
        
        #Assigns type
        self.num = num
        #creates spritecheet for blue bubble
        if num == 1:
            self.sprites.append(pygame.image.load('blueBub5.png'))
            self.sprites.append(pygame.image.load('blueBub4.png'))
            self.sprites.append(pygame.image.load('blueBub3.png'))
            self.sprites.append(pygame.image.load('blueBub2.png'))
            self.sprites.append(pygame.image.load('blueBub.png'))
        #Creates spritesheet for green bubble
        elif num == 2:
            self.sprites.append(pygame.image.load('greenBub5.png'))
            self.sprites.append(pygame.image.load('greenBub4.png'))
            self.sprites.append(pygame.image.load('greenBub3.png'))
            self.sprites.append(pygame.image.load('greenBub2.png'))
            self.sprites.append(pygame.image.load('greenBub.png'))
        #Creates spritesheet for red bubble
        elif num == 3:
            self.sprites.append(pygame.image.load('redBub5.png'))
            self.sprites.append(pygame.image.load('redBub4.png'))
            self.sprites.append(pygame.image.load('redBub3.png'))
            self.sprites.append(pygame.image.load('redBub2.png'))
            self.sprites.append(pygame.image.load('redBub.png'))
            
        #Sets current frame
        self.current_sprite = len(self.sprites) - 1
        self.image = self.sprites[self.current_sprite]
        #self.image = image
        
        #Creates hitbox
        self.rect = self.image.get_rect()
        self.rect.center = [pos[0],pos[1]]
        
        
        #Gets x position for the bubble
        self.x_pos = pos[0]
        #Gets y position for the bubble
        self.y_pos = pos[1]
        #Redundancy for lack of imag
        
        
        #Creates boundary for bubble
        #self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    #Starts pop animation
    def popBub(self):
        self.pop_animation = True

    #Displays bubble object and moves through frames
    def update(self, speed):
        if self.pop_animation == True:
            if(self.set_zero == False):
                self.current_sprite = 0
                self.set_zero = True
            #print(self.current_sprite)
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = len(self.sprites) - 1
                self.pop_animation = False
        
        self.image = self.sprites[int(self.current_sprite)]
        
    #Checks if bubble is pressed
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    #Changes color of bubble
    def changeColor(self):
        #Remembers old type
        self.old = self.num
        #Creates new type
        self.num = (random.randint(1, 3))
        #Empty spritesheet
        self.sprites = []
        
        #Pop frames for blue
        if self.old == 1:
            self.sprites.append(pygame.image.load('blueBub6.png'))
            self.sprites.append(pygame.image.load('blueBub7.png'))
        #Pop frames for green
        elif self.old == 2:
            self.sprites.append(pygame.image.load('greenBub6.png'))
            self.sprites.append(pygame.image.load('greenBub7.png'))
        #Pop frames for red
        elif self.old == 3:
            self.sprites.append(pygame.image.load('redBub6.png'))
            self.sprites.append(pygame.image.load('redBub7.png'))
        
        #Creates new animation frames for blue bubble
        if self.num == 1:
            self.sprites.append(pygame.image.load('blueBub5.png'))
            self.sprites.append(pygame.image.load('blueBub4.png'))
            self.sprites.append(pygame.image.load('blueBub3.png'))
            self.sprites.append(pygame.image.load('blueBub2.png'))
            self.sprites.append(pygame.image.load('blueBub.png'))
        #Creates new animation frames for green bubble
        elif self.num == 2:
            self.sprites.append(pygame.image.load('greenBub5.png'))
            self.sprites.append(pygame.image.load('greenBub4.png'))
            self.sprites.append(pygame.image.load('greenBub3.png'))
            self.sprites.append(pygame.image.load('greenBub2.png'))
            self.sprites.append(pygame.image.load('greenBub.png'))
        #Creates new animation frames for red bubble
        elif self.num == 3:
            self.sprites.append(pygame.image.load('redBub5.png'))
            self.sprites.append(pygame.image.load('redBub4.png'))
            self.sprites.append(pygame.image.load('redBub3.png'))
            self.sprites.append(pygame.image.load('redBub2.png'))
            self.sprites.append(pygame.image.load('redBub.png'))
            
        #Sets current frame
        self.current_sprite = len(self.sprites) - 1
        self.image = self.sprites[self.current_sprite]
        
        #Resets animation
        self.pop_animation = True
        self.set_zero = False