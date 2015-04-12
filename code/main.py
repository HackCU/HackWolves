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

def main():
    pygame.display.init()
    pygame.font.init()
    
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("THIS GAME IS AWESOME!")
    done = False
    clock = pygame.time.Clock()
	
    transitionScreen,load = titleScreen.titleScreen(done, screen, clock)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if transitionScreen == "blobScreen":
            transitionScreen = blobScreen.blobScreen(done, screen, clock)
        if transitionScreen == "playScreen":
            transitionScreen = playScreen.playGame(done, screen, clock, load)
        if transitionScreen == "titleScreen":
            transitionScreen, load = titleScreen.titleScreen(done, screen, clock)
        if transitionScreen == "optionsScreen":
            transitionScreen = optionsScreen.options(done, screen, clock)
        if transitionScreen == "unimplemented":
            transitionScreen = unimplementedScreen.unimplemented(done, screen, clock)
        if transitionScreen == "done":
            done = True
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
