import pygame
from helpers import *

def options(done, screen, clock):
    transitionScreen = None
    while not done:
        (mouseX, mouseY) = (0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print "Mousex:", mouseX, "MouseY:", mouseY
                if mouseX > 100 and mouseX < 350:
                    if mouseY > 400 and mouseY < 475:
                        print "1"
                    elif mouseY > 500 and mouseY < 625:
                        print "2"
                elif mouseX > 425 and mouseX < 675:
                    if mouseY > 400 and mouseY < 475:
                        print "3"
                    elif mouseY > 500 and mouseY < 625:
                        transitionScreen = "titleScreen"
        if transitionScreen != None:
            return transitionScreen
        else:
            screen.fill(WHITE)
            StartButton = TransitionButton(100, 400, "BUTTON1", screen)
            LoadButton = TransitionButton(100, 500, "BUTTON2", screen)
            OptionsButton = TransitionButton(425, 400, "BUTTON3", screen)
            ExitButton = TransitionButton(425, 500, "Return to Title Screen", screen)
            
            TitleFont = pygame.font.SysFont('Calibri', 100, True, False)
            TitleText = TitleFont.render("Options", True, BLACK)
            screen.blit(TitleText, [(150),(100)])
        clock.tick(60)
        pygame.display.flip()
    return "done"
