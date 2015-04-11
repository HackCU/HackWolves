import pygame
from helpers import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Player,self).__init__()
        
        self.image, self.rect = load_image('HardHatGuy.png', -1)
        self.alive = True
        self.change_x = 0
        self.change_y = 0
        self.level = None
    
    def update(self):
        self.calc_grav()
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y
         
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                
            self.change_y = 0
            
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
        
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
                
       
    def go_left(self):
        self.change_x = -10
    def go_right(self):
        self.change_x = 10
    def stop(self):
        self.change_x = 0
    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list)
        self.rect.y -= 2
        
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
         
