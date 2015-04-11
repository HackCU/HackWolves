import pygame
from helpers import *

def titleScreen(done, screen, clock):
    while not done:
        (mouseX, mouseY) = (0, 0)
        transitionScreen = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print "Mousex:", mouseX, "MouseY:", mouseY
                if mouseX > 100 and mouseX < 350:
                    if mouseY > 400 and mouseY < 475:
                        transitionScreen = "blobScreen"
                    elif mouseY > 500 and mouseY < 625:
                        print "Load Save Button"
                elif mouseX > 425 and mouseX < 675:
                    if mouseY > 400 and mouseY < 475:
                        print "Options Button"
                        transitionScreen = "optionsScreen"
                    elif mouseY > 500 and mouseY < 625:
                        transitionScreen = "done"
        if transitionScreen == None:
            screen.fill(WHITE)
            StartButton = TransitionButton(100, 400, "Start Game", screen)
            LoadButton = TransitionButton(100, 500, "Load Save", screen)
            OptionsButton = TransitionButton(425, 400, "Options", screen)
            ExitButton = TransitionButton(425, 500, "Exit", screen)
            
            TitleFont = pygame.font.SysFont('Calibri', 100, True, False)
            TitleText = TitleFont.render("HACK_WOLVES", True, BLACK)
            SubtitleText = TitleFont.render("Title TBD", True, BLACK)
            screen.blit(TitleText, [(150),(100)])
            screen.blit(SubtitleText, [(150),(200)])
        if transitionScreen != None:
            return transitionScreen
        
        clock.tick(60)
        pygame.display.flip()
    return "done"
