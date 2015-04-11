import os, sys
import pygame
from pygame.locals import *

#Globals
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class TransitionButton():
    #location
    locationX = None
    locationY = None
    #rectangle/sprite
    form = None
    #text
    text = None
    def __init__(self, valueX, valueY, string, screen):
        self.locationX = valueX
        self.locationY = valueY
        self.form = pygame.draw.rect(screen, BLACK, [valueX,valueY,250,75], 2)
        font = pygame.font.SysFont('Calibri', 40, True, False)
        self.text = font.render(string, True, BLACK)
        screen.blit(self.text, [(valueX+25),(valueY+25)])
    
    #likely unnecessary
    def update(self, string):
		print "Transition to:", string
		if string == "blobs":
			return "blobs"

class Blob():
    #location
    locationX = None
    locationY = None
    screen = None
    #rectangle/sprite
    form = None
    #text
    text = None
    def __init__(self, valueX, valueY, string, screen):
        self.locationX = valueX
        self.locationY = valueY
        self.colorFill = BLACK
        self.screen = screen
        self.form = pygame.draw.rect(screen, self.colorFill, [self.locationX,self.locationY,100,50], 2)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.text = font.render(string, True, BLACK)
        screen.blit(self.text, [(self.locationX+5),(self.locationY+10)])
        
    def updateColor(self, clickValue):
        if clickValue == True:
            self.colorFill = RED
        elif clickValue == False:
            self.colorFill = BLACK
            
    def updatePosition(self, valueX, valueY):
        self.locationX = valueX
        self.locationY = valueY
        self.form = pygame.draw.rect(self.screen, self.colorFill, [self.locationX,self.locationY,100,50], 2)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        screen = self.screen
        screen.blit(self.text, [(self.locationX+5),(self.locationY+10)])	
            
    def refreshPosition(self):
        self.form = pygame.draw.rect(self.screen, self.colorFill, [self.locationX,self.locationY,100,50], 2)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        screen = self.screen
        screen.blit(self.text, [(self.locationX+5),(self.locationY+10)])		

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
