#Screens
#Table of Contents:
#   Title Screen
#   Unimplemented Screen
#   Options Screen
#   Exit Screen
#   Ability Screen
#   Play Screen

import pygame
import cPickle as pickle
import Helpers
from Helpers import *

import Levels
import Player
import AbilityObject


"""     Title Screen: entry screen for the app      """
def titleScreen(done, clock):
    load = False
    while not done:
        (mouseX, mouseY) = (0, 0)
        transitionScreen = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX > 100 and mouseX < 350:
                    if mouseY > 400 and mouseY < 475:
                        transitionScreen = "buildingScreen"
                        load = False
                    elif mouseY > 500 and mouseY < 625:
                        transitionScreen = "playScreen"
                        load = True
                elif mouseX > 425 and mouseX < 675:
                    if mouseY > 400 and mouseY < 475:
                        transitionScreen = "optionsScreen"
                    elif mouseY > 500 and mouseY < 625:
                        transitionScreen = "done"
        if transitionScreen == None:
            screen.fill(BACKGROUND)
            StartButton = TransitionButton(100, 400, "Start Game")
            LoadButton = TransitionButton(100, 500, "Load Save")
            OptionsButton = TransitionButton(425, 400, "Options")
            ExitButton = TransitionButton(425, 500, "Exit")
            
            TeamFont = pygame.font.SysFont('Calibri', 100, True, False)
            PresentsFont = pygame.font.SysFont('Calibri', 75, True, False)
            TitleFont = pygame.font.SysFont('Calibri', 150, True, False)
            
            TeamText = TeamFont.render("Team HackWolves", True, BLACK)
            PresentsText = PresentsFont.render("presents:", True, BLACK)
            TitleText = TitleFont.render("Codeventures!", True, BLACK)
            
            screen.blit(TeamText, [(90),(50)])
            screen.blit(PresentsText, [(275),(125)])
            screen.blit(TitleText, [(30),(200)])
        if transitionScreen != None:
            return transitionScreen, load
        
        clock.tick(60)
        pygame.display.flip()
    return "done", load


"""     Unimplemented Screen: placeholder for future yet-to-be implemented screens      """
def unimplemented(done, clock):
    transitionScreen = "titleScreen"
    clicked = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        screen.fill(BACKGROUND)
        ExitButton = TransitionButton(425, 500, "Main Menu")
        
        TitleFont = pygame.font.SysFont('Calibri', 60, True, False)
        TitleText = TitleFont.render("This function isn't implemented yet;", True, BLACK)
        SubtitleText = TitleFont.render("please try another function.", True, BLACK)
        screen.blit(TitleText, [(50),(100)])
        screen.blit(SubtitleText, [(50),(200)])
        
        if transitionScreen != None and clicked == True:
            return transitionScreen
        
        clock.tick(60)
        pygame.display.flip()
    return "done"
    
"""     Options Screen: allows user to adjust some options for the game     """
def options(done, clock):
    transitionScreen = None
    while not done:
        (mouseX, mouseY) = (0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX > 100 and mouseX < 350:
                    if mouseY > 400 and mouseY < 475:
                        transitionScreen = "unimplemented"
                    elif mouseY > 500 and mouseY < 625:
                        transitionScreen = "unimplemented"
                elif mouseX > 425 and mouseX < 675:
                    if mouseY > 400 and mouseY < 475:
                        transitionScreen = "unimplemented"
                    elif mouseY > 500 and mouseY < 625:
                        transitionScreen = "titleScreen"
        if transitionScreen != None:
            return transitionScreen
        else:
            screen.fill(BACKGROUND)
            StartButton = TransitionButton(100, 400, "Button 1")
            LoadButton = TransitionButton(100, 500, "Button 2")
            OptionsButton = TransitionButton(425, 400, "Button 3")
            ExitButton = TransitionButton(425, 500, "Main Menu")
            
            TitleFont = pygame.font.SysFont('Calibri', 100, True, False)
            TitleText = TitleFont.render("Options", True, BLACK)
            screen.blit(TitleText, [(150),(100)])
        clock.tick(60)
        pygame.display.flip()
    return "done"

"""     Exit Screen: intermediary exit point for player     """
def exitScreen(done, clock):
    clicked = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        screen.fill(BACKGROUND)
        ExitButton = TransitionButton(425, 500, "Exit Game")
        
        TitleFont = pygame.font.SysFont('Calibri', 60, True, False)
        TitleText = TitleFont.render("We hope you had fun :)", True, BLACK)
        SubtitleText = TitleFont.render("Thanks for playing!", True, BLACK)
        screen.blit(TitleText, [(50),(100)])
        screen.blit(SubtitleText, [(50),(200)])
        
        if clicked == True:
            return
        
        clock.tick(60)
        pygame.display.flip()
    return "done"

"""     Building Screen: Function building display with helper functions      """
def buildingScreen(done, clock, load):

    transitionScreen = None
    
    rArrow = abilityButton(25, 325, AbilityObject.abilityItem("rArrow"))
    lArrow = abilityButton(25, 400, AbilityObject.abilityItem("lArrow"))
    upArrow = abilityButton(25, 475, AbilityObject.abilityItem("upArrow"))
    ifAbility = abilityButton(25, 250, AbilityObject.abilityItem("if"))
    
    MoveRight = abilityButton(25, 25, AbilityObject.abilityItem("MoveRight"))
    abilityList.append(MoveRight)
    
    abilityList.append(rArrow)
    abilityList.append(lArrow)
    abilityList.append(upArrow)
    abilityList.append(ifAbility)
    
    rArrow2 = abilityButton(25, 325, AbilityObject.abilityItem("rArrow"))
    lArrow2 = abilityButton(25, 400, AbilityObject.abilityItem("lArrow"))
    upArrow2 = abilityButton(25, 475, AbilityObject.abilityItem("upArrow"))
    ifAbility2 = abilityButton(25, 250, AbilityObject.abilityItem("if"))
    
    MoveRight2 = abilityButton(25, 25, AbilityObject.abilityItem("MoveRight"))
    abilityList.append(MoveRight2)
    
    abilityList.append(rArrow2)
    abilityList.append(lArrow2)
    abilityList.append(upArrow2)
    abilityList.append(ifAbility2)
    
    selectedAbility = None
    clicked = False
    
    
    recentlySelected = None
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if 175 < mouseX and mouseX < 625 and 125 < mouseY and mouseY < 575:
                    (positionX, positionY) = findPositionInArray(mouseX, mouseY)
                    if workspaceArray[positionX][positionY] != "":
                        workspaceArray[positionX][positionY] = ""
                selectedAbility = findAbilityButton(abilityList, mouseX, mouseY)
                if selectedAbility != None:
                    recentlySelected = selectedAbility
                if clicked == True:
                    clicked = False
                else:
                    clicked = True
                if mouseX > 675 and mouseX < 775:
                    if mouseY > 25 and mouseY < 75:
                        # Unimplemented: Saved Fns
                        return "unimplemented", False
                    elif mouseY > 100 and mouseY < 150:
                        # Unimplemented: Save Fn
                        return "unimplemented", False
                    elif mouseY > 175 and mouseY < 225:
                        # Unimplemented: Clear workspace
                        return "unimplemented", False
                    elif mouseY > 325 and mouseY < 375:
                        return "playScreen", load
                    elif mouseY > 400 and mouseY < 450:
                        return "optionsScreen", False
                    elif mouseY > 475 and mouseY < 525:
                        return "unimplemented", False
        
        if transitionScreen != None:
            return transitionScreen
        
        screen.fill(BACKGROUND)
        
        WorkSpace1 = pygame.draw.rect(screen, BUTTON2, [175, 125, 450, 450], 0)
        WorkSpace2 = pygame.draw.rect(screen, BUTTON1, [175, 125, 450, 450], 4)
        LevelScreen1 = pygame.draw.rect(screen, BUTTON2, [200, 25, 400, 75], 0)
        LevelScreen2 = pygame.draw.rect(screen, BUTTON1, [200, 25, 400, 75], 4)
        
        horizontalStart = 200
        while horizontalStart < 525:
            pygame.draw.line(screen, BUTTON1, [175, horizontalStart], [625, horizontalStart], 4)
            horizontalStart = horizontalStart + 75
        verticalStart = 175
        while verticalStart < 625:
            pygame.draw.line(screen, BUTTON1, [verticalStart, 125], [verticalStart, 575], 4)
            verticalStart = verticalStart + 150
        
        if selectedAbility != None and clicked == True:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selectedAbility.updateColor(True)
            selectedAbility.updatePosition(mouseX, mouseY)
        elif recentlySelected != None and clicked == False:
            (X, Y) = recentlySelected.returnPosition()
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if findPositionInArray(mouseX, mouseY) != None:
                if 175 > X or X > 625 or 125 > Y or Y > 575:
                    i = 1 #filler
                else:
                    (positionX, positionY) = findPositionInArray(mouseX, mouseY)
                    snapToGrid(recentlySelected)
                    workspaceArray[positionX][positionY] = recentlySelected.generateString()
                    print workspaceArray
            if 175 > X or X > 625 or 125 > Y or Y > 575:
                (originX, originY) = recentlySelected.returnOrigin()
                recentlySelected.updatePosition(originX, originY)
            recentlySelected.updateColor(False)
            recentlySelected = None
        
        for item in abilityList:
            item.refreshPosition()
        
        Functions = smallTransitionButton(675, 25, "Open Functions")
        BindToKey = smallTransitionButton(675, 100, "Save Function")
        Clear = smallTransitionButton(675, 175, "Clear")
        Start = smallTransitionButton(675, 325, "Start")
        Options = smallTransitionButton(675, 400, "Options")
        Help = smallTransitionButton(675, 475, "Help")

        clock.tick(60)
        pygame.display.flip()
    return "done", False

"""     Play Screen: main game screen; sidescroller     """
def playGame(done, clock, load):
    mainPlayer = Player.Player()
    transitionScreen = None
    
    mainPlayer.level_list.append(Levels.Level_01(mainPlayer))
    mainPlayer.level_list.append(Levels.Level_02(mainPlayer))
    #level_list.append(levels.Level_03(mainPlayer))
    
    if load:
        mainPlayer.current_level_no, mainPlayer.rect.x, mainPlayer.rect.y, temp_world_shift = pickle.load(open("Saves/save.p", "rb"))
        mainPlayer.current_string = "Level " + str((mainPlayer.current_level_no)+1)
        mainPlayer.current_level = mainPlayer.level_list[mainPlayer.current_level_no]
        mainPlayer.current_level.world_shift = temp_world_shift
       # mainPlayer.rect.x, mainPlayer.rect.y, mainPlayer.current_level.world_shift = pickle.load(open("Saves/position.p", "rb"))
    else:
        mainPlayer.current_level = mainPlayer.level_list[mainPlayer.current_level_no]
        mainPlayer.current_string = "Level " + str((mainPlayer.current_level_no)+1)
        mainPlayer.rect.x = 50
        mainPlayer.rect.y = 0
    #current_level = level_list[current_level_no]
    
    active_sprite_list = pygame.sprite.Group()
    mainPlayer.level = mainPlayer.current_level
    
    #mainPlayer.rect.x, mainPlayer.rect.y, current_level.world_shift = pickle.load(open("position.p", "rb"))
    #mainPlayer.rect.x = 50
    #mainPlayer.rect.y = 0#SCREEN_HEIGHT - 50 - mainPlayer.rect.height
    active_sprite_list.add(mainPlayer)
    
    #current_level.shift_world(-current_level.world_shift)

    temp = mainPlayer.current_level.world_shift
    mainPlayer.current_level.world_shift = 0
    mainPlayer.current_level.shift_world(temp)
            
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pickle.dump((mainPlayer.current_level_no, mainPlayer.rect.x, mainPlayer.rect.y, mainPlayer.current_level.world_shift), open( "Saves/save.p", "wb" ) )
                #pickle.dump(blobList, open( "blobs.p", "wb" ) )
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX > 25 and mouseX < 135:
                    if mouseY > 25 and mouseY < 75:
                        transitionScreen = "buildingScreen"
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LEFT:
#                     mainPlayer.go_left()
                # if event.key == pygame.K_RIGHT:
#                     mainPlayer.go_right()


                # testString01 = "event.key == pygame.K_LEFT"
                # testString00 = "if " + testString01 +": "
                # testString11 = testString00 + "exec('mainPlayer.go_left()')"
                #
                # testString21 = "event.key == pygame.K_RIGHT"
                # testString20 = "if " + testString21 +": "
                # testString31 = testString20 + "exec('mainPlayer.go_right()')"
                (cs1,cs2,cs3) = buildCommands(workspaceArray)
                print "cs1 = " + cs1
                print "cs2 = " + cs2
                print "cs3 = " + cs3
                
                try:
                    exec(cs1)
                    exec(cs2)
                    exec(cs3)
                except:
                    print "Whoooops"
                
                # ourString = "if event.key == pygame.K_LEFT: exec('mainPlayer.go_left()')"
#                 ourString2 = "if event.key == pygame.K_RIGHT: exec('mainPlayer.go_right()')"
#                 exec(ourString +"\n" + ourString2)
                
                # if event.key == pygame.K_UP:
                #     mainPlayer.jump()
                if event.key == pygame.K_1:
                    mainPlayer.current_level_no = 0
                    mainPlayer.current_string = "Level " + str((mainPlayer.current_level_no)+1)
                    mainPlayer.current_level = mainPlayer.level_list[mainPlayer.current_level_no]
                    mainPlayer.level = mainPlayer.current_level
                    mainPlayer.rect.x = 120
                    mainPlayer.rect.y = 0
                if event.key == pygame.K_2:
                    mainPlayer.current_level_no = 1
                    mainPlayer.current_string = "Level " + str((mainPlayer.current_level_no)+1)
                    mainPlayer.current_level = mainPlayer.level_list[mainPlayer.current_level_no]
                    mainPlayer.level = mainPlayer.current_level
                    mainPlayer.rect.x = 120
                    mainPlayer.rect.y = 450
                #if event.key == pygame.K_3:
                #    current_level_no = 2
                #    currentString = "Level " + str((current_level_no)+1)
                #    current_level = level_list[current_level_no]
                #    mainPlayer.level = current_level
                #    mainPlayer.rect.x = 120
                #    mainPlayer.rect.y = 0
                
                if Helpers.Test is True:
                    print "testing"
                    if event.key == pygame.K_LEFT:
                        mainPlayer.go_left()
                    if event.key == pygame.K_RIGHT:
                        mainPlayer.go_right()
                    if event.key == pygame.K_UP:
                        mainPlayer.jump()
                        
                        
                if event.key == pygame.K_ESCAPE:

                    pickle.dump((mainPlayer.current_level_no, mainPlayer.rect.x, mainPlayer.rect.y, mainPlayer.current_level.world_shift), open("Saves/save.p", "wb" ))
                    #pickle.dump(blobList, open( "blobs.p", "wb" ) )

                    done = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and mainPlayer.change_x < 0:
                    mainPlayer.stop()
                if event.key == pygame.K_RIGHT and mainPlayer.change_x > 0:
                    mainPlayer.stop()
                    
        active_sprite_list.update()
        
        mainPlayer.current_level.update()
        
        if mainPlayer.rect.right >= 500:
            diff = mainPlayer.rect.right - 500
            mainPlayer.rect.right = 500
            mainPlayer.current_level.shift_world(-diff)
        
        if mainPlayer.rect.left <= 120:
            diff = 120 - mainPlayer.rect.left
            mainPlayer.rect.left = 120
            mainPlayer.current_level.shift_world(diff)
            
        #current_position = mainPlayer.rect.x + mainPlayer.current_level.world_shift
        #print "rect ",mainPlayer.rect.x
        #print "worldshift ", current_level.world_shift
        '''if current_position < current_level.level_limit:
            mainPlayer.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                currentString = "Level " + str((current_level_no)+1)
                current_level = level_list[current_level_no]
                mainPlayer.level = current_level
                #if current_level_no is 2:
                 #   mainPlayer.rect.x = 50
                  #  mainPlayer.rect.y = 0
            else:
                gameOver = True
        '''
        if not mainPlayer.gameOver:
            #drawing code should go here
            mainPlayer.current_level.draw()
            active_sprite_list.draw(screen)
            smallTransitionButton(25,25, "Building Screen")
            TitleFont = pygame.font.SysFont('Calibri', 25, True, False)
            TitleText = TitleFont.render(mainPlayer.current_string, True, BLACK)
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
            pickle.dump((mainPlayer.current_level_no, mainPlayer.rect.x, mainPlayer.rect.y, mainPlayer.current_level.world_shift), open( "Saves/save.p", "wb" ) )
            #pickle.dump((mainPlayer.rect.x, mainPlayer.rect.y, mainPlayer.current_level.world_shift), open( "Saves/position.p", "wb" ) )
            return "buildingScreen", True

    
    # clear?
    pickle.dump((mainPlayer.current_level_no, 340, 50, 0), open( "Saves/save.p", "wb" ) )
    return "done", False
