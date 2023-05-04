import pygame, sys, math, random

class StoreChoice():

    def __init__(self, pos, kind, option):
        self.kind = option
        scale = [150, 150]
        scale2 = [550, 73]
        self.petImages = {"blackCat": pygame.transform.scale(pygame.image.load("Images/Black Cat Choice.png"), scale),
                          "calicoCat": pygame.transform.scale(pygame.image.load("Images/Calico Cat Choice.png"), scale),
                          "owl": pygame.transform.scale(pygame.image.load("Images/Owl Choice.png"), scale),
                          "frog": pygame.transform.scale(pygame.image.load("Images/Frog Choice.png"), scale),
                          "raccoon": pygame.transform.scale(pygame.image.load("Images/Raccoon Choice.png"), scale)}
        self.potionImages = {"speed": pygame.transform.scale(pygame.image.load("Images/Speed Choice.png"), scale),
                             "health": pygame.transform.scale(pygame.image.load("Images/Health Choice.png"), scale),
                             "fullHeal": pygame.transform.scale(pygame.image.load("Images/Full Heal Choice.png"), scale),
                             "halfHeal": pygame.transform.scale(pygame.image.load("Images/Half Heal Choice.png"), scale),
                             "revive": pygame.transform.scale(pygame.image.load("Images/Revive Choice.png"), scale)}
        self.clothesImages = {"eyeSt": pygame.transform.scale(pygame.image.load("Images/Eyes Option.png"), scale2),
                              "mouthSt": pygame.transform.scale(pygame.image.load("Images/Mouths Option.png"), scale2),
                              "colorSt": pygame.transform.scale(pygame.image.load("Images/Colors Option.png"), scale2),
                              "hatSt": pygame.transform.scale(pygame.image.load("Images/Hats Option.png"), scale2),
                              "shirtSt": pygame.transform.scale(pygame.image.load("Images/Shirts Option.png"), scale2),
                              "glassSt": pygame.transform.scale(pygame.image.load("Images/Glasses Option.png"), scale2)}
        self.spellImages = {"simple": pygame.transform.scale(pygame.image.load("Images/Item Choice Template.png"), scale)}
        
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
