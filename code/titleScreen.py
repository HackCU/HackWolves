import pygame
from helpers import *

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
