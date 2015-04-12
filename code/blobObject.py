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
        
        if self.name == 'if':
            blobBlob = Blob(25, 250, self)
            blobList.append(blobBlob)
            
        elif self.name == 'rArrow':
            blobBlob = Blob(25, 325, self)
            blobList.append(blobBlob)
        
        elif self.name == 'lArrow':
            blobBlob = Blob(25, 400, self)
            blobList.append(blobBlob)
            
        elif self.name == 'upArrow':
            blobBlob = Blob(25, 475, self)
            blobList.append(blobBlob)
            
        else:
            blobBlob = Blob(25, 550, self)
            blobList.append(blobBlob)
            
        
        
        # for x in blobScreen.blobList:
#             print x
    
    def __reduce__(self):
        return (self.__class__, (self.name,))
    
    # def update(self):
    #     if self.collected:
    #         self.rect = [0,0]
        
