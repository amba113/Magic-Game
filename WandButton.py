import pygame, sys, math, random

class WandButton():

    def __init__(self, kind, pos = [25,25]):
        self.kind = kind
        
        self.images = {"basic": pygame.image.load("Images/Wands/Options/Wand1 Pic.png"),
                       "colorful": pygame.image.load("Images/Wands/Options/Wand2 Pic.png"),
                       "swirl": pygame.image.load("Images/Wands/Options/Wand3 Pic.png"),
                       "candyCane": pygame.image.load("Images/Wands/Options/Wand4 Pic.png")}
        
        self.image = self.images[kind]
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
