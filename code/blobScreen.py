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
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
                            MoveRight2 = Blob(25, 25, blobObject.blobObject("MoveRight"))
                            blobList.append(MoveRight2)
                        selectedBlob = MoveRight
                    elif mouseY > 100 and mouseY < 150:
                        print "Move Left"
                    elif mouseY > 175 and mouseY < 225:
                        print "Jump"
                    elif mouseY > 250 and mouseY < 300:
                        print "Crouch"
                # Static object, no need to update
                elif mouseX > 175 and mouseX < 625:
                    print "Level display & workspace"
                elif mouseX > 675 and mouseX < 775:
                    if mouseY > 25 and mouseY < 75:
                        # Unimplemented: Saved Fns
                        return "unimplemented"
                    elif mouseY > 100 and mouseY < 150:
                        # Unimplemented: Bind to key
                        return "unimplemented"
                    elif mouseY > 175 and mouseY < 225:
                        # Unimplemented: Clear workspace
                        return "unimplemented"
                    elif mouseY > 325 and mouseY < 375:
                        return "playScreen"
                    elif mouseY > 400 and mouseY < 450:
                        return "optionsScreen"
                    elif mouseY > 475 and mouseY < 525:
                        return "unimplemented"
        
        if transitionScreen != None:
            return transitionScreen
        
        screen.fill(BACKGROUND)
        
        WorkSpace1 = pygame.draw.rect(screen, BUTTON2, [175, 125, 450, 400], 0)
        WorkSpace2 = pygame.draw.rect(screen, BUTTON1, [175, 125, 450, 400], 4)
        LevelScreen1 = pygame.draw.rect(screen, BUTTON2, [200, 25, 400, 75], 0)
        LevelScreen2 = pygame.draw.rect(screen, BUTTON1, [200, 25, 400, 75], 4)
        pygame.draw.line(screen, BUTTON1, [175, 225], [625, 225], 4)
        pygame.draw.line(screen, BUTTON1, [175, 325], [625, 325], 4)
        pygame.draw.line(screen, BUTTON1, [175, 425], [625, 425], 4)
        
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
        
        Functions = smallTransitionButton(675, 25, "Saved Functions")
        BindToKey = smallTransitionButton(675, 100, "Bind to Key")
        Clear = smallTransitionButton(675, 175, "Clear")
        Start = smallTransitionButton(675, 325, "Start")
        Options = smallTransitionButton(675, 400, "Options")
        Help = smallTransitionButton(675, 475, "Help")

        clock.tick(60)
        pygame.display.flip()
    return "done"
