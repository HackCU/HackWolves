#Level 03
import pygame
import main
import Helpers
from Helpers import *
from BlobObject import *

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
            
        blob1 = blobObject("MoveLeft")
        blob1.rect.x = 650
        blob1.rect.y = 50
        self.blob_list.add(blob1)
        
        door = exitDoor(40, 50)
        door.rect.x = 750
        door.rect.y = 500
        door.player = self.player
        self.exit_list.add(door)
'''
