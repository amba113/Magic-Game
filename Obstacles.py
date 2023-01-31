import pygame, sys, math, random

class Obstacle():

    def __init__(self, pos = [25,25], appearance = "wall"):
        
        scale1 = [50, 50]
        scale2 = [75, 75]
        scale3 = [25, 25]
        scale4 = [75, 100]
        self.images = {"wall": pygame.transform.scale(pygame.image.load("Images/Wall.png"), scale1),
                       "tree": pygame.transform.scale(pygame.image.load("Images/Tree.png"), scale2),
                       "top": pygame.image.load("Images/TestTB.png"),
                       "bottom": pygame.image.load("Images/TestTB.png"),
                       "left": pygame.image.load("Images/TestLR.png"),
                       "right": pygame.image.load("Images/TestLR.png"),
                       "portal": pygame.image.load("Images/Portal.png"),
                       "tutorialEntrance": pygame.image.load("Images/TutDoor.png"),
                       "tutorialExit": pygame.image.load("Images/TutDoor.png"),
                       "cactus": pygame.transform.scale(pygame.image.load("Images/Cactus.png"), scale3),
                       "bush": pygame.transform.scale(pygame.image.load("Images/Bush.png"), scale4),
                       "bushClear": pygame.transform.scale(pygame.image.load("Images/BushClear.png"), scale4)}
        
        self.kind = appearance
        self.image = self.images[self.kind]
        self.rect = self.image.get_rect(center = pos)
        
    def playerCollide(self, other):
        if self.rect.right > other.rect.left - 10:
            if self.rect.left < other.rect.right + 10:
                if self.rect.bottom > other.rect.top + 10:
                    if self.rect.top < other.rect.bottom - 10:
                        if self.kind == "bush":
                            self.kind = "bushClear"
                    elif self.kind == "bush":
                        self.kind = "bush"
                elif self.kind == "bush":
                    self.kind = "bush"
            elif self.kind == "bush":
                self.kind = "bush"
        elif self.kind == "bush":
            self.kind = "bush"
        self.image = self.images[self.kind]
    def update(self):
        pass
