import pygame
import main
from helpers import *

class Level():
    platform_list = None
    enemy_list = None
    
    #how far the world has been scrolled left/right
    world_shift = 0
    
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        
    def draw(self, screen):
        screen.fill(main.BLUE)
        
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
    
    def shift_world(self, shift_x):
        self.world_shift += shift_x
        
        for platform in self.platform_list:
            platform.rect.x += shift_x
            
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            
class Platform(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        
        super(Platform,self).__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(main.GREEN)
        
        self.rect = self.image.get_rect()
        

class Level_01(Level):
    
    def __init__(self,player):
        Level.__init__(self, player)
        
        self.level_limit = -1000
        
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [550, 0, 50, 800]]
                 
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
class Level_02(Level):
    
    def __init__(self,player):
        Level.__init__(self, player)
        
        self.level_limit = -1000
        
        level = [[210, 30, 500, 500],
                 [210, 30, 800, 400],
                 [210, 30, 1000, 500],
                 [210, 30, 1120, 280]]
                 
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
