import player
import levels
import pygame
import cPickle as pickle
from helpers import *

def playGame(done, screen, clock):
    mainPlayer = player.Player()
    
    level_list = []
    level_list.append(levels.Level_01(mainPlayer))
    level_list.append(levels.Level_02(mainPlayer))
    
    #current_level_no = 0
    current_level_no = pickle.load(open("save.p", "rb"))
    current_level = level_list[current_level_no]
    
    active_sprite_list = pygame.sprite.Group()
    mainPlayer.level = current_level
    
    mainPlayer.rect.x = 340
    mainPlayer.rect.y = SCREEN_HEIGHT - 50 - mainPlayer.rect.height
    active_sprite_list.add(mainPlayer)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pickle.dump(current_level_no, open( "save.p", "wb" ) )
                done = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mainPlayer.go_left()
                if event.key == pygame.K_RIGHT:
                    mainPlayer.go_right()
                if event.key == pygame.K_UP:
                    mainPlayer.jump()
                if event.key == pygame.K_1:
                    current_level_no = 0
                    current_level = level_list[current_level_no]
                    mainPlayer.level = current_level
                if event.key == pygame.K_2:
                    current_level_no = 1
                    current_level = level_list[current_level_no]
                    mainPlayer.level = current_level
                if event.key == pygame.K_ESCAPE:
                    pickle.dump(current_level_no, open("save.p", "wb" ))
                    done = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and mainPlayer.change_x < 0:
                    mainPlayer.stop()
                if event.key == pygame.K_RIGHT and mainPlayer.change_x > 0:
                    mainPlayer.stop()
                    
        active_sprite_list.update()
        
        current_level.update()
        
        if mainPlayer.rect.right >= 500:
            diff = mainPlayer.rect.right - 500
            mainPlayer.rect.right = 500
            current_level.shift_world(-diff)
        
        if mainPlayer.rect.left <= 120:
            diff = 120 - mainPlayer.rect.left
            mainPlayer.rect.left = 120
            current_level.shift_world(diff)
        
        current_position = mainPlayer.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            mainPlayer.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                mainPlayer.level = current_level
        
        #drawing code should go here
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        #end of drawing code section    
        
        clock.tick(60)
        
        pygame.display.flip()
        
    return "done"
