import pygame
from helpers import *

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
