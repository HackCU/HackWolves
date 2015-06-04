#Level Helpers
import pygame
from . import *
#import main
#import Helpers
#from Helpers import *
#from BlobObject import *

class Platform(pygame.sprite.Sprite):
    
    def __init__(self, width, height, color,name):
        
        super(Platform,self).__init__()
        self.name = name
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        
class exitDoor(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        
        super(exitDoor,self).__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()
        
class trapDoor(pygame.sprite.Sprite):
    
    def __init__(self, width, height, color):
        
        super(trapDoor,self).__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        
