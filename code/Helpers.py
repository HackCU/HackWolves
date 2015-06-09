#Helpers
#Table of Contents:
#   Global Constants
#   Variables and Lists
#   WOO
#   Find Position
#   Snap to Grid
#   Transition Button
#   Small Transition Button
#   YAY
#   Load Image Function
#   Create String Function
#   Build Commands Function

import os, sys
import pygame
from pygame.locals import *

"""     Global Constants        """
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (42, 168, 27)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY = (102, 182, 222)
BACKGROUND = (19, 146, 237)
BUTTON1 = (209, 98, 19)
BUTTON2 = (237, 110, 19)
WORKSPACE1 = (237, 103, 33)
WORKSPACE2 = (209, 98, 19)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

"""     Variables and Lists       """

abilityList = []

OpenTrapDoor = False

workspaceArray = [["" for x in range(3)] for x in range(6)]


commandString1 = ""
commandString2 = ""
commandString3 = ""

<<<<<<< HEAD
"""     WOO     """
def findBlob(blobList, mouseX, mouseY):
    for blob in blobList:
        (X, Y) = blob.returnPosition()
=======
def findAbilityButton(abilityList, mouseX, mouseY):
    for ability in abilityList:
        (X, Y) = ability.returnPosition()
>>>>>>> 5d660ddb437a555169b5fd0579ec66c0f3f69a82
        if X < mouseX and (X+100) > mouseX:
            if Y < mouseY and (Y+50) > mouseY:
                return ability
    return None

"""     Find Position       """
def findPositionInArray(mouseX, mouseY):
    if 175 <= mouseX and mouseX < 325:
        if mouseY < 200:
            return (0,0)
        elif 200 <= mouseY < 275:
            return (1,0)
        elif 275 <= mouseY < 350:
            return (2,0)
        elif 350 <= mouseY < 425:
            return (3,0)
        elif 425 <= mouseY < 500:
            return (4,0)
        elif 500 <= mouseY < 575:
            return (5,0)
    elif 325 <= mouseX and mouseX < 475:
        if mouseY < 200:
            return (0,1)
        elif 200 <= mouseY < 275:
            return (1,1)
        elif 275 <= mouseY < 350:
            return (2,1)
        elif 350 <= mouseY < 425:
            return (3,1)
        elif 425 <= mouseY < 500:
            return (4,1)
        elif 500 <= mouseY < 575:
            return (5,1)
    elif 475 <= mouseX and mouseX < 625:
        if mouseY < 200:
            return (0,2)
        elif 200 <= mouseY < 275:
            return (1,2)
        elif 275 <= mouseY < 350:
            return (2,2)
        elif 350 <= mouseY < 425:
            return (3,2)
        elif 425 <= mouseY < 500:
            return (4,2)
        elif 500 <= mouseY < 575:
            return (5,2)
    else:
        return None

"""     Snap to Grid        """
def snapToGrid(stored):
    if stored != None:
        X, Y = stored.returnPosition()
        if 175 <= X and X < 325:
            X = 190
            if Y < 200:
                Y = 140
            elif 200 <= Y < 275:
                Y = 215
            elif 275 <= Y < 350:
                Y = 290
            elif 350 <= Y < 425:
                Y = 365
            elif 425 <= Y < 500:
                Y = 440
            elif 500 <= Y < 575:
                Y = 515
        elif 325 <= X and X < 475:
            X = 340
            if Y < 200:
                Y = 140
            elif 200 <= Y < 275:
                Y = 215
            elif 275 <= Y < 350:
                Y = 290
            elif 350 <= Y < 425:
                Y = 365
            elif 425 <= Y < 500:
                Y = 440
            elif 500 <= Y < 575:
                Y = 515
        elif 475 <= X and X < 625:
            X = 490
            if Y < 200:
                Y = 140
            elif 200 <= Y < 275:
                Y = 215
            elif 275 <= Y < 350:
                Y = 290
            elif 350 <= Y < 425:
                Y = 365
            elif 425 <= Y < 500:
                Y = 440
            elif 500 <= Y < 575:
                Y = 515
        else:
            return None
        stored.updatePosition(X,Y)
        return

"""     Transition Button       """
class TransitionButton():
    def __init__(self, valueX, valueY, string):
        self.locationX = valueX
        self.locationY = valueY
        self.form1 = pygame.draw.rect(screen, BUTTON1, [valueX,valueY,250,75], 0)
        self.form2 = pygame.draw.rect(screen, BUTTON2, [valueX,valueY,250,75], 4)
        font = pygame.font.SysFont('Calibri', 40, True, False)
        self.text = font.render(string, True, BLACK)
        screen.blit(self.text, [(valueX+25),(valueY+25)])

"""     Small Transition Button     """
class smallTransitionButton():
    def __init__(self, valueX, valueY, string):
        self.locationX = valueX
        self.locationY = valueY
        self.form1 = pygame.draw.rect(screen, BUTTON1, [valueX,valueY,115,50], 0)
        self.form2 = pygame.draw.rect(screen, BUTTON2, [valueX,valueY,115,50], 2)
        font = pygame.font.SysFont('Calibri', 20, True, False)
        self.text = font.render(string, True, BLACK)
        screen.blit(self.text, [(valueX+5),(valueY+10)])

<<<<<<< HEAD
"""     YAY     """
class Blob():
    def __init__(self, valueX, valueY, blobObject):
=======
class abilityButton():
    def __init__(self, valueX, valueY, abilityObject):
>>>>>>> 5d660ddb437a555169b5fd0579ec66c0f3f69a82
        self.locationX = valueX
        self.locationY = valueY
        self.originX = valueX
        self.originY = valueY
        self.colorFill = BUTTON2
        self.colorText = BLACK
        self.screen = screen

        self.ability = abilityObject
        self.form1 = pygame.draw.rect(screen, BUTTON1, [self.locationX,self.locationY,100,50], 0)
        self.form2 = pygame.draw.rect(screen, self.colorFill, [self.locationX,self.locationY,100,50], 2)

        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.text = font.render(abilityObject.name, True, self.colorText)
        screen.blit(self.text, [(self.locationX+5),(self.locationY+10)])
        
        self.name = abilityObject.name
        self.string = ""
    
    def provideName(self):
        return self.name
    
    def returnOrigin(self):
        valueX = self.originX
        valueY = self.originY
        return (valueX, valueY)
    
    def __reduce__(self):
        return (self.__class__, (self.locationX, self.locationY, self.ability))
        
    def generateString(self):
        if self.name == "Default":
            self.string = "TESTING - Default Generation"
        if self.name == "MoveRight":
            self.string = "MoveRight"
        if self.name == "MoveLeft":
            self.string = "MoveLeft"
        if self.name == "Jump":
            self.string = "Jump"
        if self.name == "lArrow":
            self.string = "lArrow"
        if self.name == "rArrow":
            self.string = "rArrow"
        if self.name == "upArrow":
            self.string = "upArrow"
        if self.name == "if":
            self.string = "if"
        return self.string
        
        
        
    def updateColor(self, clickValue):
        if clickValue == True:
            self.colorFill = RED
            self.colorText = RED
        elif clickValue == False:
            self.colorFill = BUTTON1
            self.colorText = BLACK
            
    def updatePosition(self, valueX, valueY):
        self.locationX = valueX
        self.locationY = valueY
        self.form1 = pygame.draw.rect(self.screen, BUTTON1, [self.locationX,self.locationY,100,50], 0)
        self.form2 = pygame.draw.rect(self.screen, self.colorFill, [self.locationX,self.locationY,100,50], 2)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        screen = self.screen
        screen.blit(self.text, [(self.locationX+5),(self.locationY+10)])	
            
    def refreshPosition(self):
        self.form1 = pygame.draw.rect(self.screen, BUTTON1, [self.locationX,self.locationY,100,50], 0)
        self.form2 = pygame.draw.rect(self.screen, self.colorFill, [self.locationX,self.locationY,100,50], 2)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        screen = self.screen
        screen.blit(self.text, [(self.locationX+5),(self.locationY+10)])
    
    def returnPosition(self):
        valueX = self.locationX
        valueY = self.locationY
        return (valueX, valueY)

"""     Load Image Function     """
def load_image(name, colorkey=None):
    fullname = os.path.join('Resources', 'Images')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)
    return image, image.get_rect()
    
"""     Create String Function     """
def createString(name, array, i, j):
    
    string = ""
    
    if name == "if":
        print "Found if"
        string = "if " + createString(array[i][j+1],array, i, j+1) +":"
    
    if name == "MoveRight":
        string = "exec('mainPlayer.go_right()')"
    if name == "MoveLeft":
        print "Found MoveLeft"
        string = "exec('mainPlayer.go_left()')"
    if name == "Jump":
        string = "exec('mainPlayer.jump()')"
        
    if name == "rArrow":
        string = "event.key == pygame.K_RIGHT"
    if name == "lArrow":
        print "Found lArrow"
        string = "event.key == pygame.K_LEFT"
    if name == "upArrow":
        string = "event.key == pygame.K_UP"
        
    return string

"""     Build Commands Function     """
def buildCommands(array):
    
    commandString1 = ""
    commandString2 = ""
    commandString3 = ""
    
    for i in range(0,5):
        for j in range(0,2):
            
            if array[i][j] != "":
                if j==0:
                    print "TESTING ---- " + commandString1
                    if array[i][j] == "if":
                        if commandString1 == "":
                            commandString1 = createString(array[i][j], array, i, j) + createString(array[i+1][j+1], array, i+1, j+1)
                            # print commandString1
                            
                        elif commandString2 == "":
                            print "Yeppers"
                            commandString2 = createString(array[i][j], array, i, j) + createString(array[i+1][j+1], array, i+1, j+1)
                            print commandString1
                            
                        else:
                            print "Sures"
                            commandString3 = createString(array[i][j], array, i, j) + createString(array[i+1][j+1], array, i+1, j+1)

        
    return (commandString1, commandString2, commandString3)
