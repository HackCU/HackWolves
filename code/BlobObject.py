#AbilityObject
import pygame
from Helpers import *

class blobObject(pygame.sprite.Sprite):
    
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
        self.name = name
        
        self.collected = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def collect(self):
        self.collected = True
        
        if self.name == 'if':
            blobBlob = Blob(25, 250, self)
            blobList.append(blobBlob)
            
            blobBlob1 = Blob(25, 250, self)
            blobList.append(blobBlob1)
            blobBlob2 = Blob(25, 250, self)
            blobList.append(blobBlob2)
            
        elif self.name == 'rArrow':
            blobBlob = Blob(25, 325, self)
            blobList.append(blobBlob)
            
            blobBlob1 = Blob(25, 325, self)
            blobList.append(blobBlob1)
            blobBlob2 = Blob(25, 325, self)
            blobList.append(blobBlob2)
        
        elif self.name == 'lArrow':
            blobBlob = Blob(25, 400, self)
            blobList.append(blobBlob)
            
            blobBlob1 = Blob(25, 400, self)
            blobList.append(blobBlob1)
            blobBlob2 = Blob(25, 400, self)
            blobList.append(blobBlob2)
            
        elif self.name == 'upArrow':
            blobBlob = Blob(25, 475, self)
            blobList.append(blobBlob)
            
            blobBlob1 = Blob(25, 475, self)
            blobList.append(blobBlob1)
            blobBlob2 = Blob(25, 475, self)
            blobList.append(blobBlob2)
            
        elif self.name == "MoveRight":
            blobBlob = Blob(25, 25, self)
            blobList.append(blobBlob)
            
            blobBlob1 = Blob(25, 25, self)
            blobList.append(blobBlob1)
            blobBlob2 = Blob(25, 25, self)
            blobList.append(blobBlob2)
        
        elif self.name == "MoveLeft":
            blobBlob = Blob(25, 100, self)
            blobList.append(blobBlob)
            
            blobBlob1 = Blob(25, 100, self)
            blobList.append(blobBlob1)
            blobBlob2 = Blob(25, 100, self)
            blobList.append(blobBlob2)
            
        elif self.name == "Jump":
            blobBlob = Blob(25, 175, self)
            blobList.append(blobBlob)
            
            blobBlob1 = Blob(25, 175, self)
            blobList.append(blobBlob1)
            blobBlob2 = Blob(25, 175, self)
            blobList.append(blobBlob2)
            
        else:
            blobBlob = Blob(25, 550, self)
            blobList.append(blobBlob)
    
    def __reduce__(self):
        return (self.__class__, (self.name,))
    
