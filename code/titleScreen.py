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

pygame.draw.rect(screen, BLACK, [175, 125, 450, 400], 2)
font = pygame.font.SysFont('Calibri', 25, True, False)
self.text = font.render("HACK_WOLVES", True, BLACK)
screen.blit(self.text, [(350),(250)])
