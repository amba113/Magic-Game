import pygame, sys, math

class Item():
    def __init__(self, pos = [25,25], kind = "wand", char = '!'):
        
        self.images = {"wand": pygame.image.load("Images/Wands/Art/Wand.png"),
                       "halfHealPotion": pygame.image.load("Images/Shown/Potions/HalfHealthPotion.png"),
                       "fullHealPotion": pygame.image.load("Images/Shown/Potions/FullHealthPotion.png"),
                       "speedPotion": pygame.image.load("Images/Shown/Potions/SpeedPotion.png"),
                       "revivePotion": pygame.image.load("Images/Shown/Potions/RevivePotion.png"),
                       "healthPotion": pygame.image.load("Images/Shown/Potions/HealthPotion.png"),
                       "Spell2": pygame.image.load("Images/Shown/Spells/Spell 2.png"),
                       "singleCoin": pygame.image.load("Images/Shown/Coins/Coin.png")}
        
        self.kind = kind
        self.char = char
        self.image = self.images[self.kind]
        self.rect = self.image.get_rect(center = pos)
        self.damage = 3
