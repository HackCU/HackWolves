import pygame
import unimplementedScreen
import titleScreen
import player
import playScreen
import blobScreen
import levels
import optionsScreen
import cPickle as pickle
from helpers import *

def exitScreen(done, screen, clock):
    clicked = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        screen.fill(BACKGROUND)
        ExitButton = TransitionButton(425, 500, "Exit Game", screen)
        
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

def main():
    pygame.display.init()
    pygame.font.init()
    
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("THIS GAME IS AWESOME!")
    done = False
    clock = pygame.time.Clock()
	
    transitionScreen,load = titleScreen.titleScreen(done, clock)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if transitionScreen == "blobScreen":
            transitionScreen = blobScreen.blobScreen(done, clock)
        if transitionScreen == "playScreen":
            transitionScreen = playScreen.playGame(done, clock, load)
        if transitionScreen == "titleScreen":
            transitionScreen, load = titleScreen.titleScreen(done, clock)
        if transitionScreen == "optionsScreen":
            transitionScreen = optionsScreen.options(done, clock)
        if transitionScreen == "unimplemented":
            transitionScreen = unimplementedScreen.unimplemented(done, clock)
        if transitionScreen == "done":
            exitScreen(done, screen, clock)
            done = True
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
