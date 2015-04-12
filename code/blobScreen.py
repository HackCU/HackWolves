import pygame
from helpers import *
import player
import blobObject

#selected_particle = findParticle(my_particles, mouseX, mouseY)
#if selected_particle:
#	selected_particle.color = (255,0,0)
#	(mouseX, mouseY) = pygame.mouse.get_pos()
#	selected_particle.x = mouseX
#	selected_particle.y = mouseY

def findBlob(blobList, mouseX, mouseY):
    for blob in blobList:
        (X, Y) = blob.returnPosition()
        if X < mouseX and (X+100) > mouseX:
            if Y < mouseY and (Y+50) > mouseY:
                return blob
    return None
        
def blobScreen(done, clock):
    transitionScreen = None
    
    MoveRight = Blob(25, 25, blobObject.blobObject("MoveRight"))
    MoveLeft = Blob(25, 100, blobObject.blobObject("MoveLeft"))
    Jump = Blob(25, 175, blobObject.blobObject("Jump"))
    # Crouch = Blob(25, 250, blobObject.blobObject("Crouch"))
    blobList.append(MoveRight)
    blobList.append(MoveLeft)
    blobList.append(Jump)
    # blobList.append(Crouch)

    selectedBlob = None
    clicked = False
    
    workspaceArray = [[0 for x in range(3)] for x in range(6)]
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                selectedBlob = findBlob(blobList, mouseX, mouseY)
                if clicked == True:
                    clicked = False
                elif clicked == False:
                    clicked = True
                # Static object, no need to update
                if mouseX > 675 and mouseX < 775:
                    if mouseY > 25 and mouseY < 75:
                        # Unimplemented: Saved Fns
                        return "unimplemented"
                    elif mouseY > 100 and mouseY < 150:
                        # Unimplemented: Save Fn
                        return "unimplemented"
                    elif mouseY > 175 and mouseY < 225:
                        # Unimplemented: Clear workspace
                        return "unimplemented"
                    elif mouseY > 325 and mouseY < 375:
                        return "playScreen", True
                    elif mouseY > 400 and mouseY < 450:
                        return "optionsScreen"
                    elif mouseY > 475 and mouseY < 525:
                        return "unimplemented"
        
        if transitionScreen != None:
            return transitionScreen
        
        screen.fill(BACKGROUND)
        
        WorkSpace1 = pygame.draw.rect(screen, BUTTON2, [175, 125, 450, 450], 0)
        WorkSpace2 = pygame.draw.rect(screen, BUTTON1, [175, 125, 450, 450], 4)
        LevelScreen1 = pygame.draw.rect(screen, BUTTON2, [200, 25, 400, 75], 0)
        LevelScreen2 = pygame.draw.rect(screen, BUTTON1, [200, 25, 400, 75], 4)
        
        horizontalStart = 200
        while horizontalStart < 525:
            pygame.draw.line(screen, BUTTON1, [175, horizontalStart], [625, horizontalStart], 4)
            horizontalStart = horizontalStart + 75
        verticalStart = 175
        while verticalStart < 625:
            pygame.draw.line(screen, BUTTON1, [verticalStart, 125], [verticalStart, 575], 4)
            verticalStart = verticalStart + 150
        
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
        
        Functions = smallTransitionButton(675, 25, "Open Functions")
        BindToKey = smallTransitionButton(675, 100, "Save Function")
        Clear = smallTransitionButton(675, 175, "Clear")
        Start = smallTransitionButton(675, 325, "Start")
        Options = smallTransitionButton(675, 400, "Options")
        Help = smallTransitionButton(675, 475, "Help")

        clock.tick(60)
        pygame.display.flip()
    return "done"
