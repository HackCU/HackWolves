import pygame
import main
import helpers
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
        self.trap_list = pygame.sprite.Group()
        self.player = player
        
        
    def update(self):
        #if not helpers.collected:
            #print "here2"
        self.platform_list.update()
        #else:
         #   print "here"
          #  self.platform_list.remove(self.trapDoor)
        self.platform_list.update()
        self.enemy_list.update()
        self.exit_list.update()
        self.blob_list.update()
        self.trap_list.update()
        
    def draw(self):
        screen.fill(SKY)
        
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.exit_list.draw(screen)
        self.trap_list.draw(screen)
        for item in self.blob_list:
            possessed = False
            for item2 in blobList:
                if item.name is item2.name:
                    possessed = True
            if not possessed:
                item.draw(screen)
    
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
            
        for trap in self.trap_list:
            trap.rect.x += shift_x
                
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
        
class Level_01(Level):
    def __init__(self,player):
        Level.__init__(self, player)
        
        self.level_limit = -1000
        
        #level = [[210, 70, 500, 450],
        #         [210, 70, 800, 350],
        #         [210, 70, 1000, 450],
        #         [210, 70, 1120, 230],
        #         [3500, 50, -1000, 550]]
        
        level = [[300, 100, 0, 100],
                 [300, 350, 400, 100],
                 [200, 600, -150, 0],
                 [200, 100, 200, 350],
                 [100, 500, 700, -50],
                 [3500, 50, -1000, 550]]        
        
        for platform in level:
            block = Platform(platform[0], platform[1], GREEN,"platform")
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
        '''wall = Platform(1, 550, SKY)
        wall.rect.x = 0
        wall.rect.y = 0
        wall.player = self.player
        self.platform_list.add(wall)    
        '''
        
        trap = trapDoor(100, 1, GREEN)
        trap.rect.x = 300
        trap.rect.y = 100
        trap.player = self.player
        self.trap_list.add(trap)
            
        blob1 = blobObject("MoveLeft")
        blob1.rect.x = 650
        blob1.rect.y = 50
        self.blob_list.add(blob1)
        
        '''blob2 = blobObject("rArrow")
        blob2.rect.x = 1300
        blob2.rect.y = 500
        self.blob_list.add(blob2)
        
        blob3 = blobObject("lArrow")
        blob3.rect.x = 1500
        blob3.rect.y = 400
        self.blob_list.add(blob3)
        
        blob4 = blobObject("upArrow")
        blob4.rect.x = 900
        blob4.rect.y = 400
        self.blob_list.add(blob4)
        '''
        
        
        door = exitDoor(40, 50)
        door.rect.x = 750
        door.rect.y = 500
        door.player = self.player
        self.exit_list.add(door)

    
                
class Level_02(Level):
    def __init__(self,player):
        Level.__init__(self, player)
        
        self.level_limit = -1000
        
        level = [[210, 70, 500, 450],
                 [210, 70, 800, 350],
                 [210, 70, 1000, 450],
                 [210, 70, 1120, 230],
                 [3500, 50, -1000, 550]]
        
              
        
        for platform in level:
            block = Platform(platform[0], platform[1], GREEN,"platform")
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
        wall = Platform(1, 550, SKY,"platform")
        wall.rect.x = -50
        wall.rect.y = 0
        wall.player = self.player
        self.platform_list.add(wall)    
        
          
        blob1 = blobObject("Jump")
        blob1.rect.x = 400
        blob1.rect.y = 500
        self.blob_list.add(blob1)
        
        '''trapDoor = Platform(100, 1, GREEN)
        trapDoor.rect.x = 300
        trapDoor.rect.y = 100
        trapDoor.player = self.player
        self.platform_list.add(trapDoor)
        
        blob1 = blobObject("lArrow")
        blob1.rect.x = 650
        blob1.rect.y = 50
        self.blob_list.add(blob1)
        
        blob2 = blobObject("rArrow")
        blob2.rect.x = 1300
        blob2.rect.y = 500
        self.blob_list.add(blob2)
        
        blob3 = blobObject("lArrow")
        blob3.rect.x = 1500
        blob3.rect.y = 400
        self.blob_list.add(blob3)
        
        blob4 = blobObject("upArrow")
        blob4.rect.x = 900
        blob4.rect.y = 400
        self.blob_list.add(blob4)
        '''
        
        
        door = exitDoor(40, 50)
        door.rect.x = 1900
        door.rect.y = 500
        door.player = self.player
        self.exit_list.add(door)
'''    
class Level_03(Level):
    
    def __init__(self,player):
        Level.__init__(self, player)
        
        self.level_limit = -1000
        
        #level = [[210, 70, 500, 450],
        #         [210, 70, 800, 350],
        #         [210, 70, 1000, 450],
        #         [210, 70, 1120, 230],
        #         [3500, 50, -1000, 550]]
        
        level = [[300, 100, 0, 100],
                 [300, 350, 400, 100],
                 [200, 600, -150, 0],
                 [200, 100, 200, 350],
                 [100, 500, 700, -50],
                 [3500, 50, -1000, 550]]        
        
        for platform in level:
            block = Platform(platform[0], platform[1], GREEN,"platform")
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
        
        
        trap = trapDoor(100, 1, GREEN)
        trap.rect.x = 300
        trap.rect.y = 100
        trap.player = self.player
        self.trap_list.add(trap)
            
        blob1 = blobObject("moveLeft")
        blob1.rect.x = 650
        blob1.rect.y = 50
        self.blob_list.add(blob1)
        
        door = exitDoor(40, 50)
        door.rect.x = 750
        door.rect.y = 500
        door.player = self.player
        self.exit_list.add(door)
'''
