import pygame
from helpers import *
import blobScreen


size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
 
class blobObject(pygame.sprite.Sprite):
    
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
        self.name = name
        
        self.collected = False
        
    def collect(self):
        self.collected = True
        
        blobBlob = Blob(25, 325, self)
        blobList.append(blobBlob)
        # for x in blobScreen.blobList:
#             print x
    
    def __reduce__(self):
        return (self.__class__, (self.name))
    
    # def update(self):
    #     if self.collected:
    #         self.rect = [0,0]
        
