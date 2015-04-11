import pygame
from helpers import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('HardHatGuy.png', -1)
        self.alive = True
    
    