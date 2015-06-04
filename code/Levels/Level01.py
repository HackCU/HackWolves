#Level 01
import pygame
import main
import Helpers
from Helpers import *
from BlobObject import *

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

    
             
