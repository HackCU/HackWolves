import pygame
from helpers import *

# To hide mouse curcor (needed in main)
#pygame.mouse.set_visible(False)

#def findParticle(particles, x, y):
#	for p in particles:
#		if (in spot):
#			return p
#	return None

#selected_particle = findParticle(my_particles, mouseX, mouseY)
#if selected_particle:
#	selected_particle.color = (255,0,0)
#	(mouseX, mouseY) = pygame.mouse.get_pos()
#	selected_particle.x = mouseX
#	selected_particle.y = mouseY

pygame.init()
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Blobs")

done = False

clock = pygame.time.Clock()

class Blob():
    #location
    locationX = None
    locationY = None
    #rectangle/sprite
    form = None
    #text
    text = None
    def __init__(self, valueX, valueY, string):
        self.locationX = valueX
        self.locationY = valueY
        self.form = pygame.draw.rect(screen, BLACK, [valueX,valueY,100,50], 2)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.text = font.render(string, True, BLACK)
        screen.blit(self.text, [(valueX),(valueY)])
        
    def update(self):
        self.locationX = valueX
        self.locationY = valueY

while not done:
    (mouseX, mouseY) = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()

    screen.fill(WHITE)
    #pygame.draw.rect(screen, BLACK, [20,20,250,100], 2)
    #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
    MoveRight = Blob(25, 25, "Move Right")
    MoveLeft = Blob(25, 100, "Move Left")
    Jump = Blob(25, 175, "Jump")
    Crouch = Blob(25, 250, "Crouch")
    Functions = Blob(675, 25, "Functions")
    BindToKey = Blob(675, 100, "Bind to Key")
    Clear = Blob(675, 175, "Clear")
    Start = Blob(675, 325, "Start")
    Options = Blob(675, 400, "Options")
    Help = Blob(675, 475, "Help")
    WorkSpace = pygame.draw.rect(screen, BLACK, [175, 125, 450, 400], 2)
    LevelScreen = pygame.draw.rect(screen, BLACK, [200, 25, 400, 75], 2)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
