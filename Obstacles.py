import pygame, sys, math, random

class Obstacle():

    def __init__(self, pos = [25,25], appearance = "wall"):
        
        self.appearance = appearance
        scale1 = [50, 50]
        scale2 = [75, 75]
        scale3 = [25, 25]
        scale4 = [75, 100]
        self.images = [pygame.transform.scale(pygame.image.load("Images/Wall.png"), scale1),
                       pygame.transform.scale(pygame.image.load("Images/Tree.png"), scale2),
                       pygame.image.load("Images/TestTB.png"),
                       pygame.image.load("Images/TestLR.png"),
                       pygame.image.load("Images/Portal.png"),
                       pygame.image.load("Images/TutDoor.png"),
                       pygame.transform.scale(pygame.image.load("Images/Cactus.png"), scale3),
                       pygame.transform.scale(pygame.image.load("Images/Bush.png"), scale4)]
        
        if appearance == "wall":
            self.num = 0
        elif appearance == "tree":
            self.num = 1
        elif appearance == "top" or appearance == "bottom":
            self.num = 2
        elif appearance == "left" or appearance == "right":
            self.num = 3
        elif "portal" in appearance:
            self.num = 4
        elif appearance == "tutent" or appearance == "tutext":
            self.num = 5
        elif appearance == "cactus":
            self.num = 6
        elif appearance == "bush":
            self.num = 7
        
        self.kind = appearance
        self.image = self.images[self.num]
        self.rect = self.image.get_rect(center = pos)
        
    def update(self):
        pass
