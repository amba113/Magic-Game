import pygame, sys, math, random

class Popup():

    def __init__(self, pos = [25,25]):
        self.images = [pygame.image.load("Images/Wand Choice Box.png")]
        
        self.image = self.images[0]
        
        self.rect = self.image.get_rect(center = pos)
