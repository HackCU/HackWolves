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
        
def blobScreen(done, screen, clock):
    transitionScreen = None
    while not done:
        (mouseX, mouseY) = (0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX > 25 and mouseX < 125:
                    print "Column for blobs"
                elif mouseX > 175 and mouseX < 625:
                    print "Level display & workspace"
                elif mouseX > 675 and mouseX < 775:
                    if mouseY > 325 and mouseY < 375:
                        return "playScreen"
                    print "Transition buttons"
        
        if transitionScreen != None:
            return transitionScreen
        
        screen.fill(WHITE)
        MoveRight = Blob(25, 25, "Move Right", screen)
        MoveLeft = Blob(25, 100, "Move Left", screen)
        Jump = Blob(25, 175, "Jump", screen)
        Crouch = Blob(25, 250, "Crouch", screen)
        Functions = Blob(675, 25, "Functions", screen)
        BindToKey = Blob(675, 100, "Bind to Key", screen)
        Clear = Blob(675, 175, "Clear", screen)
        Start = Blob(675, 325, "Start", screen)
        Options = Blob(675, 400, "Options", screen)
        Help = Blob(675, 475, "Help", screen)
        WorkSpace = pygame.draw.rect(screen, BLACK, [175, 125, 450, 400], 2)
        LevelScreen = pygame.draw.rect(screen, BLACK, [200, 25, 400, 75], 2)

        clock.tick(60)
        pygame.display.flip()
    return "done"
