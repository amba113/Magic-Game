import pygame, sys, math

class Item():
    def __init__(self, pos = [25,25], kind = "wand", char = '!'):
        
        self.wandImages = [pygame.image.load("Images/Wand.png"), 
                           pygame.image.load("Images/Wand 2.png")]
        self.potionImages = [pygame.image.load("Images/HalfHealthPotion.png"),
                             pygame.image.load("Images/FullHealthPotion.png"),
                             pygame.image.load("Images/SpeedPotion.png"),
                             pygame.image.load("Images/RevivePotion.png"),
                             pygame.image.load("Images/HealthPotion.png")]
        self.spellImages = [pygame.image.load("Images/SpellTest2.png")]
        self.coinImages = [pygame.image.load("Images/Coin.png")]
        
        self.num = 0
        if kind == "wand":
            self.images = self.wandImages
        elif "Potion" in kind:
            self.images = self.potionImages
            if kind == "halfPotion":
                self.num = 0
            elif kind == "fullPotion":
                self.num = 1
            elif kind == "speedPotion":
                self.num = 2
            elif kind == "revivePotion":
                self.num = 3
            elif kind == "healthPotion":
                self.num = 4
        elif "Spell" in kind:
            self.images = self.spellImages
            if kind == "Spell2":
                self.num = 0
        elif kind == "coin":
            self.images = self.coinImages
            self.num = 0
        
        
        self.kind = kind
        self.char = char
        self.image = self.images[self.num]
        self.rect = self.image.get_rect(center = pos)
        self.damage = 3
