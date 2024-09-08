#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 07:15:39 2023

@author: parthmehta
"""
#Imports
import pygame
from button import Button
from bubble import Bubble
from background import Background
from pygame import mixer
from leaderboard import Leaderboard
import random
from powroc import PowRoc

#This project was absolute pain, pls give me 100...

#Initialize PyGame
pygame.init()
#Size of game window
X = 1250
Y = 700
#Just some constants for some positioning
MAIN_X = X//2
STARTBUTT_Y = 200
LEADBUTT_Y = 325
HOWBUTT_Y = 450
QUITBUTT_Y = 575
#Creates the screen
screen = pygame.display.set_mode((X,Y))
#Creates a caption for the window
pygame.display.set_caption("Bubble Busters")
#Just some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
#Makes the background color white
screen.fill(WHITE)


#Main Game Page
def startGame():
    #Sets Background
    background = Background(pos=(625, 350))
    #Variable for coins, score, and turns
    score = 0
    coins = 0
    turns = 20
    #User input text
    user_text = ''
    #Sets power-up
    pow = 0
    
    #rickroll easteregg
    rick = pygame.mixer.Sound("rick.mp3")
    #Important sounds for the game
    powUp = pygame.mixer.Sound("select.mp3")
    powDown = pygame.mixer.Sound("deselect.mp3")
    wrongSound = pygame.mixer.Sound("wrongSound.mp3")
    fireSound = pygame.mixer.Sound("fireSound.mp3")
    bombSound = pygame.mixer.Sound("bombSound.mp3")
    popSound = pygame.mixer.Sound("popSound.mp3")
    
    #used to set the frame rate
    clock = pygame.time.Clock()
    
    #Boolean to see if game is paused
    paused = False
    #Boolean to see if game is finished
    finished = False
    #Boolean to see if direction menu should be showing
    showDirections = False
    #Font for text
    font = pygame.font.Font('freesansbold.ttf', 32)
    #Matrix for bubbles
    matrix = []
    #Starting y position for bubbles
    bub_y = 175
    
    #Saves how many power-ups are used
    powsUsed = []
    
    #Creates group of all bubble sprites
    bub_sprites = pygame.sprite.Group()
    
    #Creates row of bubbles
    for row in range(5):
        #Starting x position for bubbles in each row
        bub_x = 210
        #Row array
        a = []
        # A for loop for column entries
        for column in range(12):   
            #Sets the type for each bubble randomly
            type = (random.randint(1, 3))
            #print(type)
            #Creates bubble objects
            a.append(Bubble(type, pos=(bub_x,bub_y)))
            
            #Changes x value for new bubbles
            bub_x += 75
        #Changes y values for new bubbles
        bub_y += 75
        #Appends the column of bubbles to the array
        matrix.append(a)
        
    #Creates each bubble sprite
    for row in range(5):
        for column in range(12):
            bub_sprites.add(matrix[row][column])
    
    #All the pictures and buttons for when game is paused
    pauseMenu = Button(image=pygame.image.load('pauseMen.png').convert(), pos=(MAIN_X, 350))
    resumeButt = Button(image=pygame.image.load('resume.png').convert(), pos=(MAIN_X, 300))
    howToButt = Button(image=pygame.image.load('gameHow.png').convert(), pos=(MAIN_X, 400))
    leaveButt = Button(image=pygame.image.load('leave.png').convert(), pos=(MAIN_X, 500))
    helpMenu = Button(image=pygame.image.load('how3.png').convert(), pos=(MAIN_X, 350))
    resumeButt2 = Button(image=pygame.image.load('resume.png').convert(), pos=(MAIN_X, 550))
    #All the pictures and buttons on the main game area
    PUASEBUTT = Button(image=pygame.image.load('pause2.png'), pos=(1100, 50))
    LINEBUTT = Button(image=pygame.image.load('line.png'), pos=(MAIN_X - 225, 600))
    MINUSBUTT = Button(image=pygame.image.load('minus3.png'), pos=(MAIN_X - 75, 600))
    PLUSBUTT = Button(image=pygame.image.load('plus2.png'), pos=(MAIN_X + 75, 600))
    BOMBBUTT = Button(image=pygame.image.load('bomb3.png'), pos=(MAIN_X + 225, 600))
    #All the pictures and buttons on the end screen
    overMenu = Button(image=pygame.image.load('over.png').convert(), pos=(MAIN_X, 350))
    restartButt = Button(image=pygame.image.load('restart.png').convert(), pos=(MAIN_X - 100, 525))
    homeButt = Button(image=pygame.image.load('home.png').convert(), pos=(MAIN_X + 100, 525))
    #Text that prompts user to enter their name
    enterName = pygame.font.Font('freesansbold.ttf', 16).render("Enter your Name", True, "black")
    enterRect = enterName.get_rect(center = (MAIN_X, 365))
    
    #Hidden button for rickroll easteregg
    skip_rect = pygame.Rect(1000, 600, 250, 100)
    #Rectangle for player name input
    input_rect = pygame.Rect(MAIN_X - 25, 405, 50, 50)
    
    #First power up price
    FIRST_TEXT = font.render("50", True, "White")
    FIRST_RECT = pygame.Rect(385, 660, 50, 50)
    #Second power up price
    SEC_TEXT = font.render("100", True, "White")
    SEC_RECT = pygame.Rect(525, 660, 50, 50)
    #Third power up price
    THIR_TEXT = font.render("200", True, "White")
    THIR_RECT = pygame.Rect(675, 660, 50, 50)
    #Fourth power up price
    FOUR_TEXT = font.render("400", True, "White")
    FOUR_RECT = pygame.Rect(825, 660, 50, 50)
    
    
    #Forever loop while game is running, might change to optimize game
    print('start')  
    while True:
        #Sets framerate - Decreases creates lag, Increases creates lag
        clock.tick(45)
        
        #Changes background
        background.update(screen)
        
        #Gets position of player mouse
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        #Draws and animates each bubble
        bub_sprites.draw(screen)
        bub_sprites.update(.25)
        
        #Text for player score during the game
        SCORE_TEXT = font.render("Score", True, "Black")
        SCORE_NUM = font.render(str(score), True, "Black")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(550, 25))
        SCORENUM_RECT = SCORE_NUM.get_rect(center=(550, 75))
        #Text for how many turns the player has left
        TURN_TEXT = font.render("Turns", True, "Black")
        TURN_NUM = font.render(str(turns), True, "Black")
        TURN_RECT = TURN_TEXT.get_rect(center=(700, 25))
        TURNNUM_RECT = TURN_NUM.get_rect(center=(700, 75))
        #Text output for what the player has typed
        text_in = font.render(user_text, True, "Black")
        
        #Displays text
        screen.blit(SCORE_TEXT, SCORE_RECT)
        screen.blit(SCORE_NUM, SCORENUM_RECT)
        #Displays turns
        screen.blit(TURN_TEXT, TURN_RECT)
        screen.blit(TURN_NUM, TURNNUM_RECT)
        
        #Displays coin count
        COINS = font.render("Coins: " + str(coins), True, "Black")
        COINS_RECT = COINS.get_rect(x=50, y=25)
        screen.blit(COINS, COINS_RECT)
        
        #Displays powerup buttons
        PUASEBUTT.update(screen)
        MINUSBUTT.update(screen)
        PLUSBUTT.update(screen)
        LINEBUTT.update(screen)
        BOMBBUTT.update(screen)
        
        #Displays all power up prices
        screen.blit(FIRST_TEXT, FIRST_RECT)
        screen.blit(SEC_TEXT, SEC_RECT)
        screen.blit(THIR_TEXT, THIR_RECT)
        screen.blit(FOUR_TEXT, FOUR_RECT)
        
        #Displays pause menu
        if paused == True:
            pauseMenu.update(screen)
            resumeButt.update(screen)
            howToButt.update(screen)
            leaveButt.update(screen)
            
        #Displays direction menu
        if showDirections == True:
            helpMenu.update(screen)
            resumeButt2.update(screen)
            
        #Displays end menu
        if finished == True:
            #Text for player score at the end
            SCORE_TEXT_end = font.render("Score", True, "Black")
            SCORE_NUM_end = font.render(str(score), True, "Black")
            SCORE_RECT_end = SCORE_TEXT_end.get_rect(center=(625, 250))
            SCORENUM_RECT_end = SCORE_NUM_end.get_rect(center=(625, 300))
            overMenu.update(screen)
            restartButt.update(screen)
            homeButt.update(screen)
            #Displays final score
            screen.blit(SCORE_TEXT_end, SCORE_RECT_end)
            screen.blit(SCORE_NUM_end, SCORENUM_RECT_end)
            pygame.draw.rect(screen, "white", input_rect)
            #Expands text box to hold all text
            screen.blit(text_in, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_in.get_width()+10)
            input_rect.centerx = MAIN_X
            input_rect.centery = 405
            screen.blit(enterName, enterRect)
        #Checks if player finished
        if turns == 0:
            finished = True
        
        #Event checker
        for event in pygame.event.get():
            #Quits game is window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
            #Checks for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Checks if pause button is pushed
                if PUASEBUTT.checkForInput(OPTIONS_MOUSE_POS) and finished == False:
                    pygame.mixer.Sound.play(powUp)
                    paused = True
                #Checks if resume button is pushed
                if resumeButt.checkForInput(OPTIONS_MOUSE_POS) and paused == True and finished == False:
                    pygame.mixer.Sound.play(powUp)
                    paused = False
                #Checks if how to button is pressed
                if howToButt.checkForInput(OPTIONS_MOUSE_POS) and paused == True and finished == False:
                    pygame.mixer.Sound.play(powUp)
                    paused = False
                    showDirections = True
                #Checks if resume button in directions is pressed
                if resumeButt2.checkForInput(OPTIONS_MOUSE_POS) and showDirections == True and finished == False:
                    pygame.mixer.Sound.play(powUp)
                    paused = False
                    showDirections = False
                #Checks if leave button is pressed
                if leaveButt.checkForInput(OPTIONS_MOUSE_POS) and paused == True and finished == False:
                    pygame.mixer.Sound.play(powUp)
                    main()
                #Checks if hidden skip button is pressed
                if skip_rect.collidepoint(OPTIONS_MOUSE_POS):
                    #Rickroll easteregg
                    print("Never Gonna Give You Up")
                    pygame.mixer.Sound.play(rick)
                #Checks if restart button is pressed
                if restartButt.checkForInput(OPTIONS_MOUSE_POS) and finished == True:
                    pygame.mixer.Sound.play(powUp)
                    saveName(user_text)
                    saveScore(score)
                    startGame()
                #Checks if home button is pressed
                if homeButt.checkForInput(OPTIONS_MOUSE_POS) and finished == True:
                    pygame.mixer.Sound.play(powUp)
                    saveName(user_text)
                    saveScore(score)
                    main()
                #Checks if second power-up option is pressed
                if MINUSBUTT.checkForInput(OPTIONS_MOUSE_POS) and finished == False and paused == False and showDirections == False:
                    #Checks if already activated
                    if pow == 2:
                        pow = 0
                        pygame.mixer.Sound.play(powDown)
                    #Checks if can afford
                    elif coins >= 100:
                        pow = 2
                        pygame.mixer.Sound.play(powUp)
                    else:
                        pygame.mixer.Sound.play(wrongSound)
                #Checks if third power-up option is pressed
                if PLUSBUTT.checkForInput(OPTIONS_MOUSE_POS) and finished == False and paused == False and showDirections == False:
                    #Checks if already activated
                    if pow == 3:
                        pow = 0
                        pygame.mixer.Sound.play(powDown)
                    #Checks if can afford
                    elif coins >= 200:
                        pow = 3
                        pygame.mixer.Sound.play(powUp)
                    else:
                        pygame.mixer.Sound.play(wrongSound)
                #Checks if first power-up option is pressed
                if LINEBUTT.checkForInput(OPTIONS_MOUSE_POS) and finished == False and paused == False and showDirections == False:
                    #Checks if already activated
                    if pow == 1:
                        pow = 0
                        pygame.mixer.Sound.play(powDown)
                    #Checks if can afford
                    elif coins >= 50:
                        pow = 1
                        pygame.mixer.Sound.play(powUp)
                    else:
                        pygame.mixer.Sound.play(wrongSound)
                #Checks if fourth power-up option is pressed
                if BOMBBUTT.checkForInput(OPTIONS_MOUSE_POS) and finished == False and paused == False and showDirections == False:
                    #Checks if already activated
                    if pow == 4:
                        pow = 0
                        pygame.mixer.Sound.play(powDown)
                    #Checks if can afford
                    elif coins >= 400:
                        pow = 4
                        pygame.mixer.Sound.play(powUp)
                    else:
                        pygame.mixer.Sound.play(wrongSound)
                
                #Checks if a bubble is popped
                if paused == False and finished == False and showDirections == False:
                    for row in range(5):
                        for column in range(12):
                                #Checks if bubble popped
                            if matrix[row][column].checkForInput(OPTIONS_MOUSE_POS) and finished == False:
                                if pow == 0:
                                #Calculates points and coins when no power-up
                                    pygame.mixer.Sound.play(popSound)
                                    turns -= 1
                                    points = (checkPop(matrix, row, column, matrix[row][column].num))**2
                                    score += points
                                    coins += points//5
                                #Uses first power-up if already selected and animates
                                elif pow == 1:
                                    pygame.mixer.Sound.play(fireSound)
                                    vertiPow(matrix, row, column)
                                    score += 25
                                    coins -= 50
                                    
                                    powsUsed.append(PowRoc((matrix[row][column].x_pos, 0), 2))
                                    while powsUsed[-1].y_pos <= 700:
                                        
                                        powsUsed[-1].y_pos += 1
                                        powsUsed[-1].update(screen)
                                    
                                    powsUsed.clear()
                                    
                                    pow = 0
                                #Uses second power-up if selected and animates
                                elif pow == 2:
                                    pygame.mixer.Sound.play(fireSound)
                                    horiPow(matrix, row, column)
                                    score += 144
                                    coins -= 100
                                    
                                    powsUsed.append(PowRoc((0, matrix[row][column].y_pos), 1))
                                    while powsUsed[-1].x_pos <= 1250:
                                        
                                        powsUsed[-1].x_pos += 1
                                        powsUsed[-1].update(screen)
                                    
                                    powsUsed.clear()
                                    
                                    pow = 0
                                #Uses third power-up if selected and animates
                                elif pow == 3:
                                    pygame.mixer.Sound.play(fireSound)
                                    crossPow(matrix, row, column)
                                    score += 256
                                    coins -= 200
                                    
                                    powsUsed.append(PowRoc((matrix[row][column].x_pos, 0), 2))
                                    while powsUsed[-1].y_pos <= 700:
                                        
                                        powsUsed[-1].y_pos += 1
                                        powsUsed[-1].update(screen)
                                    
                                    powsUsed.append(PowRoc((0, matrix[row][column].y_pos), 1))
                                    while powsUsed[-1].x_pos <= 1250:
                                        
                                        powsUsed[-1].x_pos += 1
                                        powsUsed[-1].update(screen)
                                    
                                    powsUsed.clear()
                                    
                                    pow = 0
                                #Uses fourth power-up if selected and animates
                                elif pow == 4:
                                    pygame.mixer.Sound.play(bombSound)
                                    bombPow(matrix, row, column)
                                    score += 3600
                                    coins -=400
                                    
                                    powsUsed.append(PowRoc((625, 350), 3))
                                    time = 0
                                    while time <= 5:
                                        
                                        time += 5
                                        powsUsed[-1].update(screen)
                                    
                                    powsUsed.clear()
                                    
                                    pow = 0
                            
            #Keyboard type checks for text box       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                            
                    
        #updates window
        pygame.display.update()
        
#Makes changes according to second power-up
def horiPow(matrix, row, column):
    for col in range(12):
        matrix[row][col].changeColor()
#Makes changes according to first power-up
def vertiPow(matrix, row, column):
    for rows in range(5):
        matrix[rows][column].changeColor()
#Makes changes according to third power-up
def crossPow(matrix, row, column):
    for col in range(12):
        matrix[row][col].changeColor()
    for rows in range(5):
        matrix[rows][column].changeColor()
#Makes changes according to fourth power-up
def bombPow(matrix, row, column):
    for rows in range(5):
        for col in range(12):
            matrix[rows][col].changeColor()


#Saves name to save file
def saveName(name):
    with open('names.txt', 'a') as file:
        file.write('\n' + name)
#Saves score to save file
def saveScore(score):
    with open('scores.txt', 'a') as file:
        file.write('\n' + str(score))

#Checks if other bubbles also pop
def checkPop(matrix, row, column, num):
    
    poppedArr = [[row, column]]
    #print(poppedArr)
    matrix[row][column].changeColor()
    
    return 1 + checkRight(matrix, row, column, num, poppedArr) + checkLeft(matrix, row, column, num, poppedArr) + checkTop(matrix, row, column, num, poppedArr) + checkBot(matrix, row, column, num, poppedArr)

#Recursive function that checks if bubble to the right is similar
def checkRight(matrix, row, column, num, last):
    popped = 0
    
    colRight = column + 1
    poppedArr = last
    #Checks if similar
    if colRight < 12:
        if matrix[row][colRight].num == num:
            if [row, colRight] not in last:
                last.append([row,colRight])
                poppedArr = last
                #matrix[row][colRight].updateBub(screen)
                popped += checkRight(matrix, row, colRight, num, poppedArr)
                popped += checkLeft(matrix, row, colRight, num, poppedArr)
                popped += checkTop(matrix, row, colRight, num, poppedArr)
                popped += checkBot(matrix, row, colRight, num, poppedArr)
                popped += 1
                
                matrix[row][colRight].changeColor()
                
    return popped
#Recursive function to check if bubble to the left is similar
def checkLeft(matrix, row, column, num, last):
    popped = 0
    
    colLeft = column - 1
    poppedArr = last
    #Checks if similar
    if colLeft >= 0:
        if matrix[row][colLeft].num == num:
            if [row, colLeft] not in last:
                last.append([row,colLeft])
                poppedArr = last
                #matrix[row][colLeft].updateBub(screen)
                popped += checkRight(matrix, row, colLeft, num, poppedArr)
                popped += checkLeft(matrix, row, colLeft, num, poppedArr)
                popped += checkTop(matrix, row, colLeft, num, poppedArr)
                popped += checkBot(matrix, row, colLeft, num, poppedArr)
                popped += 1
                
                matrix[row][colLeft].changeColor()
        
    
    return popped
#Recursive function to check if top bubble is similar 
def checkTop(matrix, row, column, num, last):
    popped = 0
    
    rowTop = row + 1
    poppedArr = last
    #Checks if similar
    if rowTop < 5:
        if matrix[rowTop][column].num == num:
            if [rowTop, column] not in last:
                last.append([row,column])
                poppedArr = last
                #matrix[rowTop][column].updateBub(screen)
                popped += checkRight(matrix, rowTop, column, num, poppedArr)
                popped += checkLeft(matrix, rowTop, column, num, poppedArr)
                popped += checkTop(matrix, rowTop, column, num, poppedArr)
                popped += checkBot(matrix, rowTop, column, num, poppedArr)
                popped += 1
                
                matrix[rowTop][column].changeColor()
        
    
    return popped
#Recursive function to check if bottom bubble is similar
def checkBot(matrix, row, column, num, last):
    popped = 0
    
    rowBot = row - 1
    poppedArr = last
    #Checks if similar
    if rowBot >= 0:
        if matrix[rowBot][column].num == num:
            if [rowBot, column] not in last:
                last.append([row,column])
                poppedArr = last
                #matrix[rowBot][column].updateBub(screen)
                popped += checkRight(matrix, rowBot, column, num, poppedArr)
                popped += checkLeft(matrix, rowBot, column, num, poppedArr)
                popped += checkTop(matrix, rowBot, column, num, poppedArr)
                popped += checkBot(matrix, rowBot, column, num, poppedArr)
                popped += 1
                
                matrix[rowBot][column].changeColor()
        
    
    return popped

#Leaderboard section
def leadPage():
    #Font for this page
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    select = pygame.mixer.Sound("select.mp3")
    
    screen.fill(WHITE)
    
    print('start')
    
    #Shows backround for leaderboard
    leadScreen = Button(image=pygame.image.load('leadBack.png'), pos=(625,350))
    leadScreen.update(screen)
    
    stats = Leaderboard.findTop10()
    
    #Infinite Loop
    while True:
        #Gets player mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        #Prints first place
        FIRST_TEXT = font.render("First Place: " + stats[1][9] + "    " + str(stats[0][9]), True, "Black")
        FIRST_RECT = pygame.Rect(400, 225, 200, 50)
        screen.blit(FIRST_TEXT, FIRST_RECT)
        
        #Displays second place
        SECOND_TEXT = font.render("Second Place: " + stats[1][8] + "    " + str(stats[0][8]), True, "Black")
        SECOND_RECT = pygame.Rect(100, 350, 200, 50)
        screen.blit(SECOND_TEXT, SECOND_RECT)
        
        #Displays third place
        THIRD_TEXT = font.render("Third Place: " + stats[1][7] + "    " + str(stats[0][7]), True, "Black")
        THIRD_RECT = pygame.Rect(700, 350, 200, 50)
        screen.blit(THIRD_TEXT, THIRD_RECT)
        
        #displays fourth place
        FOURTH_TEXT = font.render("Fourth Place: " + stats[1][6] + "    " + str(stats[0][6]), True, "Black")
        FOURTH_RECT = pygame.Rect(100, 450, 200, 50)
        screen.blit(FOURTH_TEXT, FOURTH_RECT)
        
        #Displays fifth place
        FIFTH_TEXT = font.render("Fifth Place: " + stats[1][5] + "    " + str(stats[0][5]), True, "Black")
        FIFTH_RECT = pygame.Rect(700, 450, 200, 50)
        screen.blit(FIFTH_TEXT, FIFTH_RECT)
        
        
        #Creates back button to main menu
        BACKBUTTON = Button(image=pygame.image.load('backMen.png'), pos=(MAIN_X, QUITBUTT_Y+50))
        #Displays back button
        BACKBUTTON.update(screen)

        #Checks if event happened
        for event in pygame.event.get():
            #Checks if player closed the window
            if event.type == pygame.QUIT:
                pygame.quit()
            #checks if mouse is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Checks if back button is pressed
                if BACKBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Sound.play(select)
                    main()
        #Updates pygame window
        pygame.display.update()

#Code for how to page
def howPage():
    
    screen.fill(WHITE)
    #Sound effect
    select = pygame.mixer.Sound("select.mp3")
    
    #Shows help info
    helpScreen = Button(image=pygame.image.load('helpBack.png'), pos=(625,350))
    helpScreen.update(screen)
    
    #Creates back button
    BACKBUTTON = Button(image=pygame.image.load('backMen.png').convert(), pos=(MAIN_X, 640))
    
    BACKBUTTON.update(screen)
    
    #Forever loop
    while True:
        #Gets mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #Checks if event happened
        for event in pygame.event.get():
            #Checks if player closed the window
            if event.type == pygame.QUIT:
                pygame.quit()
            #Checks if mouse button was pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Checks if back button was pressed
                if BACKBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Sound.play(select)
                    main()
        
        #Updates pygame window
        pygame.display.update()

#Code for main screen
def main():
    #Sets background to white
    screen.fill(WHITE)
    #Useless variable right now
    setting = 0
    
    #Sound effect
    select = pygame.mixer.Sound("select.mp3")
    #Background
    homeScreen = Button(image=pygame.image.load('mainBack.png'), pos=(625,350))
    homeScreen.update(screen)
    
    #Creates buttons for navigation
    STARTBUTTON = Button(image=pygame.image.load('start5.png'), pos=(MAIN_X,350))
    LEADBUTTON = Button(image=pygame.image.load('lead2.png'), pos=(MAIN_X, 440))
    HOWBUTTON = Button(image=pygame.image.load('how4.png'), pos=(MAIN_X, 530))
    QUITBUTTON = Button(image=pygame.image.load('quit2.png'), pos=(MAIN_X, 620))
    
    #Displays all the buttons
    for button in [STARTBUTTON, LEADBUTTON, HOWBUTTON, QUITBUTTON]:
        button.update(screen)
    
    #Forever loop
    while True:
        
        #Gets player mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        #Checks for events
        for event in pygame.event.get():
            #Checks if player closed the window
            if event.type == pygame.QUIT:
                #running = False
                #pygame.quit()
                return
            #Checks if player pressed mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if setting == 0:
                    #Checks if start button is pressed
                    if STARTBUTTON.checkForInput(MENU_MOUSE_POS):
                        #setting = 1
                        pygame.mixer.Sound.play(select)
                        startGame()
                    #Checks if leader board button is pressed
                    if LEADBUTTON.checkForInput(MENU_MOUSE_POS):
                        #setting = 2
                        pygame.mixer.Sound.play(select)
                        leadPage()
                    #Check if how to button is pressed
                    if HOWBUTTON.checkForInput(MENU_MOUSE_POS):
                        #setting = 3
                        pygame.mixer.Sound.play(select)
                        howPage()
                    #Checks if quit button is pressed
                    if QUITBUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                #No plans for this if statement yet...
                if setting == 1:
                    print("stage 1")
                
            #Updates window    
            pygame.display.update()

#Starts application            
if __name__ == '__main__':
    main()