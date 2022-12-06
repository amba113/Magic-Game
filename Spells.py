import pygame, sys, math

class Spell():
    def __init__(self, spell, speed = [0, 0], startPos = [0, 0]):
        
        self.images = []
        
        self.kind = spell
        
        if self.kind == "basic":
            self.num = 0
        
        self.image = self.images[self.num]
        
        
