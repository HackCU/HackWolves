import pygame
from Screens import *
import Player
from Levels import *
import cPickle as pickle
from Helpers import *

def main():
    pygame.display.init()
    pygame.font.init()
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Codeventures!")
    done = False
    clock = pygame.time.Clock()
	
    transitionScreen,load = titleScreen(done, clock)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if transitionScreen == "blobScreen":
            transitionScreen, load = blobScreen.blobScreen(done, clock, load)
        elif transitionScreen == "playScreen":
            transitionScreen,load = playScreen.playGame(done, clock, load)
        elif transitionScreen == "titleScreen":
            transitionScreen, load = MenuScreens.titleScreen(done, clock)
        elif transitionScreen == "optionsScreen":
            transitionScreen = MenuScreens.options(done, clock)
        elif transitionScreen == "unimplemented":
            transitionScreen = MenuScreens.unimplemented(done, clock)
        elif transitionScreen == "done":
            MenuScreens.exitScreen(done, clock)
            done = True
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
