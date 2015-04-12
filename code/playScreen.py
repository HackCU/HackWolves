import player
import levels
import pygame
import cPickle as pickle
from helpers import *

def playGame(done, clock, load):
    mainPlayer = player.Player()
    transitionScreen = None
    gameOver = False
    
    
    level_list = []
    level_list.append(levels.Level_01(mainPlayer))
    level_list.append(levels.Level_02(mainPlayer))
    
    if load:
        current_level_no = pickle.load(open("save.p", "rb"))
    else:
        current_level_no = 0
    current_level = level_list[current_level_no]
    currentString = "Level " + str((current_level_no)+1)
    
    active_sprite_list = pygame.sprite.Group()
    mainPlayer.level = current_level
    
    mainPlayer.rect.x, mainPlayer.rect.y, current_level.world_shift = pickle.load(open("position.p", "rb"))
    mainPlayer.rect.y = SCREEN_HEIGHT - 50 - mainPlayer.rect.height
    active_sprite_list.add(mainPlayer)
    
    while not done:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pickle.dump(current_level_no, open( "save.p", "wb" ) )
                #pickle.dump(blobList, open( "blobs.p", "wb" ) )
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX > 25 and mouseX < 135:
                    if mouseY > 25 and mouseY < 75:
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
                    #pickle.dump(blobList, open( "blobs.p", "wb" ) )
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
            else:
                gameOver = True
        
        if not gameOver:
            #drawing code should go here
            current_level.draw()
            active_sprite_list.draw(screen)
            smallTransitionButton(25,25, "Building Screen")
            TitleFont = pygame.font.SysFont('Calibri', 25, True, False)
            TitleText = TitleFont.render(currentString, True, BLACK)
            screen.blit(TitleText, [(700),(25)])
            #end of drawing code section    
        else:
            screen.fill(SKY)
            gameOverFont = pygame.font.SysFont('Calibri', 40, True, False)
            gameOverText = gameOverFont.render("Congratulations! You now know how to code!", True, BLACK)
            screen.blit(gameOverText, [(50), (300)])
            
        clock.tick(60)
        
        pygame.display.flip()
        
        if transitionScreen != None:
            #save position
            #pickle.dump(blobList, open( "blobs.p", "wb" ) )
            pickle.dump((mainPlayer.rect.x, mainPlayer.rect.y, current_level.world_shift), open( "position.p", "wb" ) )
            return "blobScreen"
    
    # clear?
    pickle.dump((340, 50, 0), open( "position.p", "wb" ) )
    return "done"
