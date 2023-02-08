import pygame, sys, math, random, os
from ColorLibrary import *

class Health():

    def __init__(self, pos, size, corner = 5):
        self.color = (0, 255, 0)
        self.cRad = corner
        self.height = size[0]
        self.lengthMax = size[1]
        self.length = self.lengthMax
        self.lengthMin = self.cRad * 3
        self.step = 10
        self.rect1 = pygame.rect.Rect(pos, [self.lengthMax, self.height])
        self.rect2 = pygame.rect.Rect(pos, [self.length, self.height])
    
    def update(self, pos, hp, maxhp, screen):
        
        pygame.draw.rect(screen, self.color, self.rect2, 0, self.cRad)
        pygame.draw.rect(screen, (255, 255, 255), self.rect1, 1, self.cRad)
        
        if hp != 0:
            self.length = hp/maxhp * self.lengthMax
        else:
            self.length = self.lengthMin

        self.rect2 = pygame.rect.Rect(pos[0] - self.lengthMax/2, pos[1] - 40 - self.height/2, self.length, self.height)
        self.rect1 = pygame.rect.Rect(pos[0] - self.lengthMax/2, pos[1] - 40 - self.height/2, self.lengthMax, self.height)
        
        self.color = smoothColor((255, 0, 0), (255, 100, 0), (255, 255, 0), (0, 255, 0), self.length, self.lengthMax - self.lengthMin)
