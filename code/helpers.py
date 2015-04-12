import os, sys
import pygame
from pygame.locals import *

#Globals


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

blobList = []

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

class TransitionButton():
    def __init__(self, valueX, valueY, string):
        self.locationX = valueX
        self.locationY = valueY
        self.form1 = pygame.draw.rect(screen, BUTTON1, [valueX,valueY,250,75], 0)
        self.form2 = pygame.draw.rect(screen, BUTTON2, [valueX,valueY,250,75], 4)
        font = pygame.font.SysFont('Calibri', 40, True, False)
        self.text = font.render(string, True, BLACK)
        screen.blit(self.text, [(valueX+25),(valueY+25)])

class smallTransitionButton():
    def __init__(self, valueX, valueY, string):
        self.locationX = valueX
        self.locationY = valueY
        self.form1 = pygame.draw.rect(screen, BUTTON1, [valueX,valueY,115,50], 0)
        self.form2 = pygame.draw.rect(screen, BUTTON2, [valueX,valueY,115,50], 2)
        font = pygame.font.SysFont('Calibri', 20, True, False)
        self.text = font.render(string, True, BLACK)
        screen.blit(self.text, [(valueX+5),(valueY+10)])

class Blob():
    def __init__(self, valueX, valueY, blobObject):
        self.locationX = valueX
        self.locationY = valueY
        self.colorFill = BUTTON2
        self.colorText = BLACK
        self.screen = screen

        self.blob = blobObject
        self.form1 = pygame.draw.rect(screen, BUTTON1, [self.locationX,self.locationY,100,50], 0)
        self.form2 = pygame.draw.rect(screen, self.colorFill, [self.locationX,self.locationY,100,50], 2)

        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.text = font.render(blobObject.name, True, self.colorText)
        screen.blit(self.text, [(self.locationX+5),(self.locationY+10)])
        
        self.name = blobObject.name
        self.string = ""
    
    def provideName(self):
        return self.bname
    
    def __reduce__(self):
        return (self.__class__, (self.locationX, self.locationY, self.blob))
        
    def generateString(self):
        if self.name == "Default":
            self.string = "TESTING - Default Generation"
        print self.string
        
    def updateColor(self, clickValue):
        if clickValue == True:
            self.colorFill = RED
            self.colorText = RED
        elif clickValue == False:
            self.colorFill = BUTTON2
            self.colorFill = BLACK
            
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

def load_image(name, colorkey=None):
    fullname = os.path.join('resources', 'images')
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
