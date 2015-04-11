import pygame
from helpers import *
import main

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
        
        
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
                # Stop our vertical movement
            self.change_y = 0
         
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            
            # self.rect.bottom =
            
            if self.change_x > 0:
                self.rect.bottom = self.rect.y
                self.rect.right = block.rect.left
                
            elif self.change_x < 0:
                self.rect.bottom = self.rect.y
                self.rect.left = block.rect.right
                
                
                
 
            # Move up/down
        self.rect.y += self.change_y
 
            # Check and see if we hit anything
        
            
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
        
        if self.rect.y >= main.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = main.SCREEN_HEIGHT - self.rect.height
                
       
    def go_left(self):
        self.change_x = -10
    def go_right(self):
        self.change_x = 10
    def stop(self):
        self.change_x = 0
    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        if len(platform_hit_list) > 0 or self.rect.bottom >= main.SCREEN_HEIGHT:
            self.change_y = -10
         
