import pygame
from helpers import *

def unimplemented(done, screen, clock):
    transitionScreen = "titleScreen"
    clicked = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        screen.fill(BACKGROUND)
        ExitButton = TransitionButton(425, 500, "Main Menu", screen)
        
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
