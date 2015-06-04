#File for holding the menu screens:
import pygame
from Helpers import *

#Title Screen: entry screen for the app
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
                        transitionScreen = "blobScreen"
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


#Unimplemented Screen: placeholder for future yet-to-be implemented screens
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
    
#Options Screen: allows user to adjust some options for the game
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

#Exit Screen: intermediary exit point for player
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
