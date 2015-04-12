import pygame
import main
from helpers import *
from blobObject import *

class Level():
    platform_list = None
    enemy_list = None
    exit_list = None
    blob_list = None
    
    #how far the world has been scrolled left/right
    world_shift = 0
    
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.exit_list = pygame.sprite.Group()
        self.blob_list = pygame.sprite.Group()
        self.player = player
        
        
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.exit_list.update()
        self.blob_list.update()
        
    def draw(self, screen):
        screen.fill(SKY)
        
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.exit_list.draw(screen)
        self.blob_list.draw(screen)
    
    def shift_world(self, shift_x):
        self.world_shift += shift_x
        
        for platform in self.platform_list:
            platform.rect.x += shift_x
            
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            
        for door in self.exit_list:
            door.rect.x += shift_x
            
        for blob in self.blob_list:
            blob.rect.x += shift_x
            
            
class Platform(pygame.sprite.Sprite):
    
    def __init__(self, width, height, color):
        
        super(Platform,self).__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        
class exitDoor(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        
        super(exitDoor,self).__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()
        
class Level_01(Level):
    
    def __init__(self,player):
        Level.__init__(self, player)
        
        self.level_limit = -1000
        
        level = [[210, 70, 500, 450],
                 [210, 70, 800, 350],
                 [210, 70, 1000, 450],
                 [210, 70, 1120, 230],
                 [3500, 50, -1000, 550]]
                 
        for platform in level:
            block = Platform(platform[0], platform[1], GREEN)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
        wall = Platform(1, 550, SKY)
        wall.rect.x = 0
        wall.rect.y = 0
        wall.player = self.player
        self.platform_list.add(wall)    
            
        blob1 = blobObject("default")
        blob1.rect.x = 1500
        blob1.rect.y = 500
        self.blob_list.add(blob1)
        
        door = exitDoor(40, 50)
        door.rect.x = 1900
        door.rect.y = 500
        door.player = self.player
        self.exit_list.add(door)
                
class Level_02(Level):
    
    def __init__(self,player):
        Level.__init__(self, player)
        
        self.level_limit = -1000
        
        level = [[210, 30, 500, 450],
                 [210, 30, 800, 350],
                 [210, 30, 1000, 450],
                 [210, 30, 1120, 230],
                 [3500, 50, -1000, 550]]
                 
        for platform in level:
            block = Platform(platform[0], platform[1], GREEN)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
           
        wall = Platform(1, 550, SKY)
        wall.rect.x = 0
        wall.rect.y = 0
        wall.player = self.player
        self.platform_list.add(wall) 
        
        door = exitDoor(40, 50)
        door.rect.x = 1900
        door.rect.y = 500
        door.player = self.player
        self.exit_list.add(door)
