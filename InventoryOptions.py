import pygame, sys, math, random

class InventoryChoice():

    def __init__(self, pos, kind, option):
        self.kind = option
        scale = [150, 150]
        scale2 = [50*4, 25*4]
        self.petImages = {"blackCat": pygame.transform.scale(pygame.image.load("Images/Black Cat Item.png"), scale),
                          "calicoCat": pygame.transform.scale(pygame.image.load("Images/Calico Cat Item.png"), scale),
                          "owl": pygame.transform.scale(pygame.image.load("Images/Owl Item.png"), scale),
                          "frog": pygame.transform.scale(pygame.image.load("Images/Frog Item.png"), scale),
                          "raccoon": pygame.transform.scale(pygame.image.load("Images/Raccoon Item.png"), scale)}
        self.potionImages = {"speed": pygame.transform.scale(pygame.image.load("Images/Speed Item.png"), scale),
                             "health": pygame.transform.scale(pygame.image.load("Images/Health Item.png"), scale),
                             "fullHeal": pygame.transform.scale(pygame.image.load("Images/Full Heal Item.png"), scale),
                             "halfHeal": pygame.transform.scale(pygame.image.load("Images/Half Heal Item.png"), scale),
                             "revive": pygame.transform.scale(pygame.image.load("Images/Revive Item.png"), scale)}
        self.clothesImages = {"eyes": pygame.transform.scale(pygame.image.load("Images/Eyes Text.png"), scale2),
                              "mouth": pygame.transform.scale(pygame.image.load("Images/Mouth Text.png"), scale2),
                              "color": pygame.transform.scale(pygame.image.load("Images/Color Text.png"), scale2),
                              "hat": pygame.transform.scale(pygame.image.load("Images/Hat Text.png"), scale2),
                              "shirt": pygame.transform.scale(pygame.image.load("Images/Shirt Text.png"), scale2),
                              "glasses": pygame.transform.scale(pygame.image.load("Images/Glasses Text.png"), scale2)}
        self.spellImages = {"simple": pygame.transform.scale(pygame.image.load("Images/Item Choice Template.png"), scale)}
        
        if kind == "petsIn":
            self.image = self.petImages[option]
        elif kind == "potionsIn":
            self.image = self.potionImages[option]
        elif kind == "clothesIn":
            self.image = self.clothesImages[option]
        elif kind == "spellsIn":
            self.image = self.spellImages[option]
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
