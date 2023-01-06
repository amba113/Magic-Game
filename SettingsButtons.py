import pygame, sys, math, random

class WandButton():

    def __init__(self, pos = [25,25], num = 1):
        self.kind = num
        
        self.images = [pygame.image.load("Images/Wand1 Pic.png"),
                       pygame.image.load("Images/Wand2 Pic.png"),
                       pygame.image.load("Images/Wand3 Pic.png"),
                       pygame.image.load("Images/Wand4 Pic.png")]
        
        self.image = self.images[num - 1]
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
