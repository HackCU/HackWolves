#Level Template
import pygame

import main
from LevelTemplate import *
from . import *
from LevelHelpers import *
from Helpers import *
from BlobObject import *

#import main, helpers and blobobject

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
 
