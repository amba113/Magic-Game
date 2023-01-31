import pygame, sys, math, random

class SettingsButton():

    def __init__(self, pos, kind):
        self.kind = kind
        
        self.images = {"controls": pygame.image.load("Images/Control Set Button.png"),
                       "store": pygame.image.load("Images/Store Button.png"),
                       "quit": pygame.image.load("Images/Quit Button.png"),
                       "close": pygame.image.load("Images/Store Close.png"),
                       "pets": pygame.image.load("Images/Pets Option.png"),
                       "spells": pygame.image.load("Images/Spells Option.png"),
                       "potions": pygame.image.load("Images/Potions Option.png"),
                       "clothes": pygame.image.load("Images/Clothes Option.png")}
        
        self.image = self.images[kind]
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
