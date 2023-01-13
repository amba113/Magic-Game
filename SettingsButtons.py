import pygame, sys, math, random

class SettingsButton():

    def __init__(self, pos, num = 1):
        self.kind = num
        
        self.images = [pygame.image.load("Images/Control Set Button.png"),
                       pygame.image.load("Images/Store Button.png"),
                       pygame.image.load("Images/Quit Button.png"),
                       pygame.image.load("Images/Store Close.png"),
                       pygame.image.load("Images/Pets Option.png"),
                       pygame.image.load("Images/Spells Option.png"),
                       pygame.image.load("Images/Potions Option.png"),
                       pygame.image.load("Images/Clothes Option.png")]
        
        self.image = self.images[num - 1]
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
