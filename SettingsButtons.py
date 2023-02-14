import pygame, sys, math, random

class SettingsButton():

    def __init__(self, pos, kind):
        self.kind = kind
        self.scale1 = [50, 50]
        self.scale2 = [700/2, 200/2]
        
        self.images = {"controls": pygame.image.load("Images/Control Set Button.png"),
                       "store": pygame.image.load("Images/Store Button.png"),
                       "quit": pygame.image.load("Images/Quit Button.png"),
                       "play": pygame.transform.scale(pygame.image.load("Images/Play Button.png"), self.scale2),
                       "sign": pygame.transform.scale(pygame.image.load("Images/Signin Button.png"), self.scale2),
                       "close": pygame.image.load("Images/Store Close.png"),
                       "back": pygame.transform.scale(pygame.image.load("Images/BackButton.png"), self.scale1),
                       "controlsBox": pygame.image.load("Images/Control Box.png"),
                       "reset": pygame.image.load("Images/Reset Button.png"),
                       "locked": pygame.image.load("Images/Item Locked.png"),
                       "petsSt": pygame.image.load("Images/Pets Option.png"),
                       "spellsSt": pygame.image.load("Images/Spells Option.png"),
                       "potionsSt": pygame.image.load("Images/Potions Option.png"),
                       "clothesSt": pygame.image.load("Images/Clothes Option.png"),
                       "petsIn": pygame.image.load("Images/Pets Choice.png"),
                       "spellsIn": pygame.image.load("Images/Spells Choice.png"),
                       "potionsIn": pygame.image.load("Images/Potions Choice.png"),
                       "clothesIn": pygame.image.load("Images/Clothes Choice.png")}
        
        self.image = self.images[kind]
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
