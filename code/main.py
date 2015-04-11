import pygame
import titleScreen
import player
import playScreen
import blobScreen
import levels
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
	
    transitionScreen = titleScreen.titleScreen(done, screen, clock)
    while not done:
        if transitionScreen == "blobScreen":
            transitionScreen = blobScreen.blobScreen(done, screen, clock)
        elif transitionScreen == "playScreen":
            transitionScreen = playScreen.playGame(done, screen, clock)
        elif transitionScreen == "done":
            done = True
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
