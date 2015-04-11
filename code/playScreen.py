import player
import levels
import pygame
import cPickle as pickle
from helpers import *

def playGame(done, screen, clock):
    mainPlayer = player.Player()
    transitionScreen = None
    
    level_list = []
    level_list.append(levels.Level_01(mainPlayer))
    level_list.append(levels.Level_02(mainPlayer))
    
    current_level_no = pickle.load(open("save.p", "rb"))
    current_level = level_list[current_level_no]
    currentString = "Level " + str((current_level_no)+1)
    
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX > 25 and mouseX < 150:
                    if mouseY > 25 and mouseY < 50:
                        transitionScreen = "blobScreen"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mainPlayer.go_left()
                if event.key == pygame.K_RIGHT:
                    mainPlayer.go_right()
                if event.key == pygame.K_UP:
                    mainPlayer.jump()
                if event.key == pygame.K_1:
                    current_level_no = 0
                    currentString = "Level " + str((current_level_no)+1)
                    current_level = level_list[current_level_no]
                    mainPlayer.level = current_level
                if event.key == pygame.K_2:
                    current_level_no = 1
                    currentString = "Level " + str((current_level_no)+1)
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
                currentString = "Level " + str((current_level_no)+1)
                current_level = level_list[current_level_no]
                mainPlayer.level = current_level
                
        
        #drawing code should go here
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        smallTransitionButton(25,25, "Building Screen", screen)
        TitleFont = pygame.font.SysFont('Calibri', 25, True, False)
        TitleText = TitleFont.render(currentString, True, BLACK)
        screen.blit(TitleText, [(700),(25)])
        #end of drawing code section    
        
        clock.tick(60)
        
        pygame.display.flip()
        
        if transitionScreen != None:
            return "blobScreen"
        
    return "done"
