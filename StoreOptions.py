import pygame, sys, math, random

class StoreChoice():

    def __init__(self, pos, kind, num = 1):
        self.kind = num
        scale = [150, 150]
        self.petImages = [pygame.transform.scale(pygame.image.load("Images/Black Cat Choice.png"), scale),
                          pygame.transform.scale(pygame.image.load("Images/Calico Cat Choice.png"), scale),
                          pygame.transform.scale(pygame.image.load("Images/Owl Choice.png"), scale),
                          pygame.transform.scale(pygame.image.load("Images/Frog Choice.png"), scale)]
        self.potionImages = [pygame.transform.scale(pygame.image.load("Images/Speed Choice.png"), scale),
                             pygame.transform.scale(pygame.image.load("Images/Health Choice.png"), scale),
                             pygame.transform.scale(pygame.image.load("Images/Full Heal Choice.png"), scale),
                             pygame.transform.scale(pygame.image.load("Images/Half Heal Choice.png"), scale),
                             pygame.transform.scale(pygame.image.load("Images/Revive Choice.png"), scale)]
        self.clothesImages = []
        self.spellImages = []
        
        if kind == 5:
            self.images = self.petImages
        elif kind == 6:
            self.images = self.spellImages
        elif kind == 7:
            self.images = self.potionImages
        else:
            self.images = self.clothesImages
        
        self.image = self.images[num - 1]
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
