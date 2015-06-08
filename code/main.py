import pygame
import cPickle as pickle

from AbilityObject import *
from Helpers import *
from Levels import *
from Player import *
import Screens

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
        if transitionScreen == "buildingScreen":
            transitionScreen, load = Screens.buildingScreen(done, clock, load)
        elif transitionScreen == "playScreen":
            transitionScreen,load = Screens.playGame(done, clock, load)
        elif transitionScreen == "titleScreen":
            transitionScreen, load = Screens.titleScreen(done, clock)
        elif transitionScreen == "optionsScreen":
            transitionScreen = Screens.options(done, clock)
        elif transitionScreen == "unimplemented":
            transitionScreen = Screens.unimplemented(done, clock)
        elif transitionScreen == "done":
            Screens.exitScreen(done, clock)
            done = True
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
