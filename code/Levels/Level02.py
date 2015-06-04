#Level 02
import pygame
import main
import Helpers
from Helpers import *
from BlobObject import *

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
