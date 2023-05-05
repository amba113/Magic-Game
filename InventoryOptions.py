import pygame, sys, math, random

class InventoryChoice():

    def __init__(self, pos, kind, option):
        self.kind = option
        scale = [150, 150]
        scale2 = [50*4, 25*4]
        self.petImages = {"blackCat": pygame.transform.scale(pygame.image.load("Images/Inventory/Pets/Black Cat Item.png"), scale),
                          "calicoCat": pygame.transform.scale(pygame.image.load("Images/Inventory/Pets/Calico Cat Item.png"), scale),
                          "owl": pygame.transform.scale(pygame.image.load("Images/Inventory/Pets/Owl Item.png"), scale),
                          "frog": pygame.transform.scale(pygame.image.load("Images/Inventory/Pets/Frog Item.png"), scale),
                          "raccoon": pygame.transform.scale(pygame.image.load("Images/Inventory/Pets/Raccoon Item.png"), scale)}
        self.potionImages = {"speed": pygame.transform.scale(pygame.image.load("Images/Inventory/Potions/Speed Item.png"), scale),
                             "health": pygame.transform.scale(pygame.image.load("Images/Inventory/Potions/Health Item.png"), scale),
                             "fullHeal": pygame.transform.scale(pygame.image.load("Images/Inventory/Potions/Full Heal Item.png"), scale),
                             "halfHeal": pygame.transform.scale(pygame.image.load("Images/Inventory/Potions/Half Heal Item.png"), scale),
                             "revive": pygame.transform.scale(pygame.image.load("Images/Inventory/Potions/Revive Item.png"), scale)}
        self.clothesImages = {"eyes": pygame.transform.scale(pygame.image.load("Images/Inventory/Clothes/Eyes Text.png"), scale2),
                              "mouth": pygame.transform.scale(pygame.image.load("Images/Inventory/Clothes/Mouth Text.png"), scale2),
                              "color": pygame.transform.scale(pygame.image.load("Images/Inventory/Clothes/Color Text.png"), scale2),
                              "hat": pygame.transform.scale(pygame.image.load("Images/Inventory/Clothes/Hat Text.png"), scale2),
                              "shirt": pygame.transform.scale(pygame.image.load("Images/Inventory/Clothes/Shirt Text.png"), scale2),
                              "glasses": pygame.transform.scale(pygame.image.load("Images/Inventory/Clothes/Glasses Text.png"), scale2)}
        self.spellImages = {"basic1": pygame.transform.scale(pygame.image.load("Images/Inventory/Spells/Basic 1 Item.png"), scale),
                            "basic2": pygame.transform.scale(pygame.image.load("Images/Inventory/Spells/Basic 2 Item.png"), scale)}
        
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
