import pygame
from Helpers import *
from Screens import *

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
 
class abilityItem(pygame.sprite.Sprite):
    
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
        self.name = name
        
        self.collected = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def collect(self):
        self.collected = True
        
        if self.name == 'if':
            ifAbility = abilityButton(25, 250, self)
            abilityList.append(ifAbility)
            
            ifAbility1 = abilityButton(25, 250, self)
            abilityList.append(ifAbility1)
            ifAbility2 = abilityButton(25, 250, self)
            abilityList.append(ifAbility2)
            
        elif self.name == 'rArrow':
            rightAbility = abilityButton(25, 325, self)
            abilityList.append(rightAbility)
            
            rightAbility1 = abilityButton(25, 325, self)
            abilityList.append(rightAbility1)
            rightAbility2 = abilityButton(25, 325, self)
            abilityList.append(rightAbility2)
        
        elif self.name == 'lArrow':
            leftAbility = abilityButton(25, 400, self)
            abilityList.append(leftAbility)
            
            leftAbility1 = abilityButton(25, 400, self)
            abilityList.append(leftAbility1)
            leftAbility2 = abilityButton(25, 400, self)
            abilityList.append(leftAbility2)
            
        elif self.name == 'upArrow':
            upAbility = abilityButton(25, 475, self)
            abilityList.append(upAbility)
            
            upAbility1 = abilityButton(25, 475, self)
            abilityList.append(upAbility1)
            upAbility2 = abilityButton(25, 475, self)
            abilityList.append(upAbility2)
            
        elif self.name == "MoveRight":
            moveRightAbility = abilityButton(25, 25, self)
            abilityList.append(moveRightAbility)
            
            moveRightAbility1 = abilityButton(25, 25, self)
            abilityList.append(moveRightAbility1)
            moveRightAbility2 = abilityButton(25, 25, self)
            abilityList.append(moveRightAbility2)
        
        elif self.name == "MoveLeft":
            moveLeftAbility = abilityButton(25, 100, self)
            abilityList.append(moveLeftAbility)
            
            moveLeftAbility1 = abilityButton(25, 100, self)
            abilityList.append(moveLeftAbility1)
            moveLeftAbility2 = abilityButton(25, 100, self)
            abilityList.append(moveLeftAbility2)
            
        elif self.name == "Jump":
            jumpAbility = abilityButton(25, 175, self)
            abilityList.append(jumpAbility)
            
            jumpAbility1 = abilityButton(25, 175, self)
            abilityList.append(jumpAbility1)
            jumpAbility2 = abilityButton(25, 175, self)
            abilityList.append(jumpAbility2)
            
        else:
            defaultAbility = abilityButton(25, 550, self)
            abilityList.append(defaultAbility)
    
    def __reduce__(self):
        return (self.__class__, (self.name,))
    
    # def update(self):
    #     if self.collected:
    #         self.rect = [0,0]
        
