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
                #print "Mousex:", mouseX, "MouseY:", mouseY
                if mouseX > 100 and mouseX < 350:
                    if mouseY > 400 and mouseY < 475:#startgame
                        transitionScreen = "blobScreen"
                        load = False
                    elif mouseY > 500 and mouseY < 625:#loadgame
                        transitionScreen = "playScreen"
                        load = True
                        #print "Load Save Button"
                elif mouseX > 425 and mouseX < 675:
                    if mouseY > 400 and mouseY < 475:#options
                        print "Options Button"
                        transitionScreen = "optionsScreen"
                    elif mouseY > 500 and mouseY < 625:#exit
                        transitionScreen = "done"
        if transitionScreen == None:
            screen.fill(BACKGROUND)
            StartButton = TransitionButton(100, 400, "Start Game")
            LoadButton = TransitionButton(100, 500, "Load Save")
            OptionsButton = TransitionButton(425, 400, "Options")
            ExitButton = TransitionButton(425, 500, "Exit")
            
            TitleFont = pygame.font.SysFont('Calibri', 100, True, False)
            TitleText = TitleFont.render("HACK_WOLVES", True, BLACK)
            SubtitleText = TitleFont.render("Title TBD", True, BLACK)
            screen.blit(TitleText, [(150),(100)])
            screen.blit(SubtitleText, [(150),(200)])
        if transitionScreen != None:
            return transitionScreen, load
        
        clock.tick(60)
        pygame.display.flip()
    return "done", load
