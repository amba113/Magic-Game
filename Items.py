import pygame, sys, math

class Item():
    def __init__(self, pos = [25,25], kind = "wand", char = '!'):
        
        self.images = {"wand": pygame.image.load("Images/Wand.png"),
                       "halfHealPotion": pygame.image.load("Images/HalfHealthPotion.png"),
                       "fullHealPotion": pygame.image.load("Images/FullHealthPotion.png"),
                       "speedPotion": pygame.image.load("Images/SpeedPotion.png"),
                       "revivePotion": pygame.image.load("Images/RevivePotion.png"),
                       "healthPotion": pygame.image.load("Images/HealthPotion.png"),
                       "basic2Spell": pygame.image.load("Images/SpellTest2.png"),
                       "singleCoin": pygame.image.load("Images/Coin.png")}
        
        self.kind = kind
        self.char = char
        self.image = self.images[self.kind]
        self.rect = self.image.get_rect(center = pos)
        self.damage = 3
