#main
import pygame
#import cPickle as pickle
import sys
import Helpers
from Helpers import *
import Screens

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            Helpers.Test = True
            print "testing"
            
    pygame.display.init()
    pygame.font.init()
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    pygame.display.set_caption("Codeventures!")
    done = False
    clock = pygame.time.Clock()
	
    transitionScreen,load = Screens.titleScreen(done, clock)
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
        elif transitionScreen == "changeScreenSize":
            transitionScreen = Screens.changeResolution(done, clock)
        elif transitionScreen == "done":
            Screens.exitScreen(done, clock)
            done = True
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
