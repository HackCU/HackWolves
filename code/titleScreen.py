import pygame
from helpers import *

#Globals
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.init()
pygame.font.init()
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Title Screen")

done = False

clock = pygame.time.Clock()

while not done:
    (mouseX, mouseY) = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()

    screen.fill(WHITE)
    TransitionButton(100, 400, "Start Game", screen)
    TransitionButton(100, 500, "Load Save", screen)
    TransitionButton(425, 400, "Options", screen)
    TransitionButton(425, 500, "Exit", screen)
    #pygame.draw.rect(screen, BLACK, [475, 475, 100, 50], 2)
    #textStart = font.render("Start Game", True, BLACK)
    #textExit = font.render("Exit", True, BLACK)
    #textOptions = font.render("Options", True, BLACK)
    
    TitleFont = pygame.font.SysFont('Calibri', 100, True, False)
    TitleText = TitleFont.render("HACK_WOLVES", True, BLACK)
    SubtitleText = TitleFont.render("Title TBD", True, BLACK)
    screen.blit(TitleText, [(150),(100)])
    screen.blit(SubtitleText, [(150),(200)])
    
    clock.tick(60)
    pygame.display.flip()
pygame.quit()

