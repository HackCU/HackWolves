import pygame
from helpers import *
import player
import blobObject

def findBlob(blobList, mouseX, mouseY):
    for blob in blobList:
        (X, Y) = blob.returnPosition()
        if X < mouseX and (X+100) > mouseX:
            if Y < mouseY and (Y+50) > mouseY:
                return blob
    return None
    
def findPositionInArray(mouseX, mouseY):
    if 175 < mouseX and mouseX < 325:
        if mouseY < 200:
            return (0,0)
        elif 200 < mouseY < 275:
            return (1,0)
        elif 275 < mouseY < 350:
            return (2,0)
        elif 350 < mouseY < 425:
            return (3,0)
        elif 425 < mouseY < 500:
            return (4,0)
        elif 500 < mouseY < 575:
            return (5,0)
    elif 325 < mouseX and mouseX < 475:
        if mouseY < 200:
            return (0,1)
        elif 200 < mouseY < 275:
            return (1,1)
        elif 275 < mouseY < 350:
            return (2,1)
        elif 350 < mouseY < 425:
            return (3,1)
        elif 425 < mouseY < 500:
            return (4,1)
        elif 500 < mouseY < 575:
            return (5,1)
    elif 475 < mouseX and mouseX < 625:
        if mouseY < 200:
            return (0,2)
        elif 200 < mouseY < 275:
            return (1,2)
        elif 275 < mouseY < 350:
            return (2,2)
        elif 350 < mouseY < 425:
            return (3,2)
        elif 425 < mouseY < 500:
            return (4,2)
        elif 500 < mouseY < 575:
            return (5,2)
    else:
        return None
        
def blobScreen(done, clock, load):
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
    
    workspaceArray = [["" for x in range(3)] for x in range(6)]
    recentlySelected = None
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                #if recentlySelected != None:
                if 175 < mouseX and mouseX < 625 and 125 < mouseY and mouseY < 575:
                    print "huh? mousex:", mouseX, "mousey:", mouseY
                    (positionX, positionY) = findPositionInArray(mouseX, mouseY)
                    print "posX:", positionX, "posY:", positionY
                    if workspaceArray[positionX][positionY] != "":
                        print "made it here"
                        workspaceArray[positionX][positionY] = ""
                selectedBlob = findBlob(blobList, mouseX, mouseY)
                if selectedBlob != None:
                    recentlySelected = selectedBlob
                if clicked == True:
                    clicked = False
                else:
                    clicked = True
                if mouseX > 675 and mouseX < 775:
                    if mouseY > 25 and mouseY < 75:
                        # Unimplemented: Saved Fns
                        return "unimplemented", False
                    elif mouseY > 100 and mouseY < 150:
                        # Unimplemented: Save Fn
                        return "unimplemented", False
                    elif mouseY > 175 and mouseY < 225:
                        # Unimplemented: Clear workspace
                        return "unimplemented", False
                    elif mouseY > 325 and mouseY < 375:
                        return "playScreen", load
                    elif mouseY > 400 and mouseY < 450:
                        return "optionsScreen", False
                    elif mouseY > 475 and mouseY < 525:
                        return "unimplemented", False
        
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
        elif recentlySelected != None and clicked == False:
            (X, Y) = recentlySelected.returnPosition()
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if findPositionInArray(mouseX, mouseY) != None:
                if 175 > X or X > 625 or 125 > Y or Y > 575:
                    print "nope"
                else:
                    (positionX, positionY) = findPositionInArray(mouseX, mouseY)
                    print "what?", recentlySelected.generateString()
                    workspaceArray[positionX][positionY] = recentlySelected.generateString()
            print "workspaceArray:", workspaceArray
            if 175 > X or X > 625 or 125 > Y or Y > 575:
                (originX, originY) = recentlySelected.returnOrigin()
                recentlySelected.updatePosition(originX, originY)
            recentlySelected.updateColor(False)
            recentlySelected = None
        
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
    return "done", False
