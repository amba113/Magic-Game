import pygame, sys, math, random

class StoreChoice():

    def __init__(self, pos, kind, option):
        self.kind = option
        scale = [150, 150]
        self.petImages = {"blackCat": pygame.transform.scale(pygame.image.load("Images/Black Cat Choice.png"), scale),
                          "calicoCat": pygame.transform.scale(pygame.image.load("Images/Calico Cat Choice.png"), scale),
                          "owl": pygame.transform.scale(pygame.image.load("Images/Owl Choice.png"), scale),
                          "frog": pygame.transform.scale(pygame.image.load("Images/Frog Choice.png"), scale)}
        self.potionImages = {"speed": pygame.transform.scale(pygame.image.load("Images/Speed Choice.png"), scale),
                             "health": pygame.transform.scale(pygame.image.load("Images/Health Choice.png"), scale),
                             "fullHeal": pygame.transform.scale(pygame.image.load("Images/Full Heal Choice.png"), scale),
                             "halfHeal": pygame.transform.scale(pygame.image.load("Images/Half Heal Choice.png"), scale),
                             "revive": pygame.transform.scale(pygame.image.load("Images/Revive Choice.png"), scale)}
        self.clothesImages = {"simple": pygame.transform.scale(pygame.image.load("Images/Item Choice Template.png"), scale)}
        self.spellImages = {"simple": pygame.transform.scale(pygame.image.load("Images/Item Choice Template.png"), scale)}
        
        if kind == "pets":
            self.image = self.petImages[option]
        elif kind == "potions":
            self.image = self.potionImages[option]
        elif kind == "clothes":
            self.image = self.clothesImages[option]
        elif kind == "spells":
            self.image = self.spellImages[option]
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
