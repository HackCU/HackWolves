import pygame
import Helpers
from Helpers import *
import main

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Player,self).__init__()
        
        self.image, self.rect = load_image('HardHatGuy.png', -1)
        self.alive = True
        self.change_x = 0
        self.change_y = 0
        self.level = None
        self.blobs = []
    
    def update(self):
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
        
        # Collectin' blobs
        blob_hit_list = pygame.sprite.spritecollide(self, self.level.blob_list, True)
        for blob in blob_hit_list:
            if blob.name is "MoveLeft":
                Helpers.collected = True
                #print "collected"
            blob.collect()

 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            #print "name ",block.name
            #if block.name is "trapdoor":
             #   block1 = pygame.sprite.spritecollide(self,block, True)
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
            
        #hopefully exit collision
        exit_hit_list = pygame.sprite.spritecollide(self, self.level.exit_list, False)
        for ex in exit_hit_list:
            mainPlayer.rect.x = 120
            if playGame.current_level_no < len(playGame.level_list)-1:
                playGame.current_level_no += 1
                playGame.currentString = "Level " + str((playGame.current_level_no)+1)
                playGame.current_level = playGame.level_list[playGame.current_level_no]
                playGame.mainPlayer.level = playGame.current_level
                #if current_level_no is 2:
                 #   mainPlayer.rect.x = 50
                  #  mainPlayer.rect.y = 0
            else:
                playGame.gameOver = True
        
        if Helpers.collected:
            block_hit_list = pygame.sprite.spritecollide(self, self.level.trap_list, True)
        else:
            block_hit_list = pygame.sprite.spritecollide(self, self.level.trap_list, False)
        for block in block_hit_list:
 

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
              

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
         
