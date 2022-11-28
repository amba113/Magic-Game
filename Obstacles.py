import pygame, sys, math, random

class Obstacle():
    def __init__(self, pos = [25,25], appearance = "wall"):
        
        scale1 = [50, 50]
        scale2 = [75, 75]
        self.images = [pygame.transform.scale(pygame.image.load("Images/Wall.png"), scale1),
                       pygame.transform.scale(pygame.image.load("Images/Tree.png"), scale2),
                       pygame.image.load("Images/TestTB.png"),
                       pygame.image.load("Images/TestLR.png")]
        
        if appearance == "wall":
            self.num = 0
        elif appearance == "tree":
            self.num = 1
        elif appearance == "TB":
            self.num = 2
        elif appearance == "LR":
            self.num = 3
        
        self.image = self.images[self.num]
        self.rect = self.image.get_rect(center = pos)
        
    def update(self, size):
        pass
