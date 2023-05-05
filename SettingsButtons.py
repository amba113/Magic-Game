import pygame, sys, math, random

class SettingsButton():

    def __init__(self, pos, kind):
        self.kind = kind
        self.scale1 = [50, 50]
        self.scale2 = [700/2, 200/2]
        self.scale3 = [100, 100]
        self.scale4 = [100*2.5, 50*2.5]
        
        self.images = {"controls": pygame.image.load("Images/Settings/Options/Control Set Button.png"),
                       "store": pygame.image.load("Images/Settings/Options/Store Button.png"),
                       "signout": pygame.image.load("Images/Settings/Options/Signout Button.png"),
                       "quit": pygame.image.load("Images/Settings/Options/Quit Button.png"),
                       "play": pygame.transform.scale(pygame.image.load("Images/Start/Play Button.png"), self.scale2),
                       "sign": pygame.transform.scale(pygame.image.load("Images/Start/SignIn/Signin Button.png"), self.scale2),
                       "close": pygame.image.load("Images/Overlap/Store Close.png"),
                       "back": pygame.transform.scale(pygame.image.load("Images/Overlap/BackButton.png"), self.scale1),
                       "forward": pygame.transform.flip(pygame.transform.scale(pygame.image.load("Images/Overlap/BackButton.png"), self.scale1), True, False),
                       "back+": pygame.transform.scale(pygame.image.load("Images/Overlap/BackButton.png"), self.scale3),
                       "forward+": pygame.transform.flip(pygame.transform.scale(pygame.image.load("Images/Overlap/BackButton.png"), self.scale3), True, False),
                       "controlsBox": pygame.image.load("Images/Controls/Control Box.png"),
                       "reset": pygame.image.load("Images/Controls/Reset Button.png"),
                       "locked": pygame.image.load("Images/Inventory/Item Locked.png"),
                       "equipped": pygame.image.load("Images/Inventory/Item Equipped.png"),
                       "petsSt": pygame.image.load("Images/Store/Options/Pets Option.png"),
                       "spellsSt": pygame.image.load("Images/Store/Options/Spells Option.png"),
                       "potionsSt": pygame.image.load("Images/Store/Options/Potions Option.png"),
                       "clothesSt": pygame.image.load("Images/Store/Options/Clothes Option.png"),
                       "petsIn": pygame.image.load("Images/Inventory/Options/Pets Choice.png"),
                       "spellsIn": pygame.image.load("Images/Inventory/Options/Spells Choice.png"),
                       "potionsIn": pygame.image.load("Images/Inventory/Options/Potions Choice.png"),
                       "clothesIn": pygame.image.load("Images/Inventory/Options/Clothes Choice.png"),
                       "passSee": pygame.image.load("Images/Start/SignIn/Pass See.png"),
                       "passHide": pygame.image.load("Images/Start/SignIn/Pass Hide.png"),
                       "buy": pygame.transform.scale(pygame.image.load("Images/Store/Buttons/Buy Button.png"), self.scale4)}
        
        self.image = self.images[kind]
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
