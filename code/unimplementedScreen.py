import pygame
from helpers import *

def unimplemented(done, screen, clock):
    click = False
    transitionScreen = "titleScreen"
    while not done:
        (mouseX, mouseY) = (0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                click = True
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
        screen.fill(BACKGROUND)
        StartButton = TransitionButton(100, 400, "Start Game", screen)
        LoadButton = TransitionButton(100, 500, "Load Save", screen)
        OptionsButton = TransitionButton(425, 400, "Options", screen)
        ExitButton = TransitionButton(425, 500, "Exit", screen)
        
        TitleFont = pygame.font.SysFont('Calibri', 60, True, False)
        TitleText = TitleFont.render("This function isn't implemented yet;", True, BLACK)
        SubtitleText = TitleFont.render("please try another function.", True, BLACK)
        screen.blit(TitleText, [(50),(100)])
        screen.blit(SubtitleText, [(50),(200)])
        
        if transitionScreen != None and click == True:
            return transitionScreen
        
        clock.tick(60)
        pygame.display.flip()
    return "done"
