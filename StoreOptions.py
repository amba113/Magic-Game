import pygame, sys, math, random

class StoreChoice():

    def __init__(self, pos, kind, option, factor = 1):
        self.kind = option
        scale = [150, 150]
        scale2 = [550, 73]
        scale3 = [10 * factor, 10 * factor]
        self.petImages = {"blackCat": pygame.transform.scale(pygame.image.load("Images/Store/Pets/Black Cat Choice.png"), scale),
                          "calicoCat": pygame.transform.scale(pygame.image.load("Images/Store/Pets/Calico Cat Choice.png"), scale),
                          "owl": pygame.transform.scale(pygame.image.load("Images/Store/Pets/Owl Choice.png"), scale),
                          "frog": pygame.transform.scale(pygame.image.load("Images/Store/Pets/Frog Choice.png"), scale),
                          "raccoon": pygame.transform.scale(pygame.image.load("Images/Store/Pets/Raccoon Choice.png"), scale)}
        self.potionImages = {"speed": pygame.transform.scale(pygame.image.load("Images/Store/Potions/Speed Choice.png"), scale),
                             "health": pygame.transform.scale(pygame.image.load("Images/Store/Potions/Health Choice.png"), scale),
                             "fullHeal": pygame.transform.scale(pygame.image.load("Images/Store/Potions/Full Heal Choice.png"), scale),
                             "halfHeal": pygame.transform.scale(pygame.image.load("Images/Store/Potions/Half Heal Choice.png"), scale),
                             "revive": pygame.transform.scale(pygame.image.load("Images/Store/Potions/Revive Choice.png"), scale)}
        self.clothesImages = {"eyeSt": pygame.transform.scale(pygame.image.load("Images/Store/Options/Eyes Option.png"), scale2),
                              "mouthSt": pygame.transform.scale(pygame.image.load("Images/Store/Options/Mouths Option.png"), scale2),
                              "colorSt": pygame.transform.scale(pygame.image.load("Images/Store/Options/Colors Option.png"), scale2),
                              "hatSt": pygame.transform.scale(pygame.image.load("Images/Store/Options/Hats Option.png"), scale2),
                              "shirtSt": pygame.transform.scale(pygame.image.load("Images/Store/Options/Shirts Option.png"), scale2),
                              "glassSt": pygame.transform.scale(pygame.image.load("Images/Store/Options/Glasses Option.png"), scale2)}
        self.spellImages = {"hidden": pygame.transform.scale(pygame.image.load("Images/Store/Spells/Hidden.png"), scale3)}
        
        if kind == "petsSt":
            self.image = self.petImages[option]
        elif kind == "potionsSt":
            self.image = self.potionImages[option]
        elif kind == "clothesSt":
            self.image = self.clothesImages[option]
        elif kind == "spellsSt":
            self.image = self.spellImages[option]
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False
