import pygame, sys, math

class Item():
    def __init__(self, pos = [25,25], kind = "wand"):
        
        self.wandImages = [pygame.image.load("Images/Wand.png")]
        self.potionImages = [pygame.image.load("Images/HalfHealthPotion.png"),
                             pygame.image.load("Images/FullHealthPotion.png"),
                             pygame.image.load("Images/SpeedPotion.png")]
        
        self.num = 0
        #Gonna make image change based on choice etc
        if kind == "wand":
            self.images = self.wandImages
        elif "Potion" in kind:
            self.images = self.potionImages
            if kind == "halfPotion":
                self.num = 0
            elif kind == "fullPotion":
                self.num = 1
            else:
                self.num = 2
        
        
        self.kind = kind
        self.image = self.images[self.num]
        self.rect = self.image.get_rect(center = pos)
        self.damage = 3
        
