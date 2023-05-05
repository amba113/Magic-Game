import pygame, sys, math, random

class Popup():

    def __init__(self, kind, pos = [25, 25]):
        self.images = {"wandChoice": pygame.image.load("Images/Wand Choice Box.png"),
                       "store": pygame.image.load("Images/Store Back.png"),
                       "controls": pygame.image.load("Images/Controls Back.png"),
                       "inventory": pygame.transform.scale(pygame.image.load("Images/Inventory Back.png"),[700, 500]),
                       "escape": pygame.image.load("Images/Escape.png")}
        
        self.image = self.images[kind]
        
        self.rect = self.image.get_rect(center = pos)
