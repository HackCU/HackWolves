import pygame
from helpers import *

class blobObject(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
        self.collected = False
        
    def collect(self):
        self.collected = True
    
    
    def update(self):
        if self.collected:
            self.rect = [0,0]
        