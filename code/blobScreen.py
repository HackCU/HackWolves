import pygame
from helpers import *

#selected_particle = findParticle(my_particles, mouseX, mouseY)
#if selected_particle:
#	selected_particle.color = (255,0,0)
#	(mouseX, mouseY) = pygame.mouse.get_pos()
#	selected_particle.x = mouseX
#	selected_particle.y = mouseY
        
def blobScreen(done, screen, clock):
    transitionScreen = None
    
    blobList = []
    MoveRight = Blob(25, 25, "Move Right", screen)
    MoveLeft = Blob(25, 100, "Move Left", screen)
    Jump = Blob(25, 175, "Jump", screen)
    Crouch = Blob(25, 250, "Crouch", screen)
    blobList.append(MoveRight)
    blobList.append(MoveLeft)
    blobList.append(Jump)
    blobList.append(Crouch)
    
    selectedBlob = None
    clicked = False
    #(mouseX, mouseY) = (0, 0)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if clicked == True:
                    clicked = False
                elif clicked == False:
                    clicked = True
                if mouseX > 25 and mouseX < 125:
                    if mouseY > 25 and mouseY < 75:
                        print "Move Right"
                        if selectedBlob == None:
                            blobList.remove(MoveRight)
                            MoveRight2 = Blob(25, 25, "Move Right", screen)
                            blobList.append(MoveRight2)
                        selectedBlob = MoveRight
                    elif mouseY > 100 and mouseY < 150:
                        print "Move Left"
                    elif mouseY > 175 and mouseY < 225:
                        print "Jump"
                    elif mouseY > 250 and mouseY < 300:
                        print "Crouch"
                elif mouseX > 175 and mouseX < 625:
                    print "Level display & workspace"
                elif mouseX > 675 and mouseX < 775:
                    if mouseY > 325 and mouseY < 375:
                        return "playScreen"
                    print "Transition buttons"
        
        if transitionScreen != None:
            return transitionScreen
        
        screen.fill(WHITE)
        
        if selectedBlob != None and clicked == True:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selectedBlob.updateColor(True)
            selectedBlob.updatePosition(mouseX, mouseY)
        elif selectedBlob != None and clicked == False:
            selectedBlob.updateColor(False)
            blobList.append(selectedBlob)
            selectedBlob = None
                
        for item in blobList:
            item.refreshPosition()
        
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
