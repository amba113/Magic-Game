import pygame, sys, math, random

class Popup():

    def __init__(self, pos = [25,25], num = 0):
        self.images = [pygame.image.load("Images/Wand Choice Box.png"),
                       pygame.image.load("Images/Store Back.png")]
        
        self.image = self.images[num]
        
        self.rect = self.image.get_rect(center = pos)
