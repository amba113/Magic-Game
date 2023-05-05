import pygame, sys, math, random

class Obstacle():

    def __init__(self, pos = [25,25], appearance = "wall"):
        
        scale1 = [50, 50]
        scale2 = [75, 75]
        scale3 = [25, 25]
        scale4 = [75, 100]
        self.images = {"wall": pygame.transform.scale(pygame.image.load("Images/Shown/NIntObstacles/Wall.png"), scale1),
                       "tree": pygame.transform.scale(pygame.image.load("Images/Shown/NIntObstacles/Tree.png"), scale2),
                       "top": pygame.image.load("Images/Shown/Doors/TestTB.png"),
                       "bottom": pygame.image.load("Images/Shown/Doors/TestTB.png"),
                       "left": pygame.image.load("Images/Shown/Doors/TestLR.png"),
                       "right": pygame.image.load("Images/Shown/Doors/TestLR.png"),
                       "portal1": pygame.image.load("Images/Shown/Doors/Portal.png"),
                       "portal2": pygame.image.load("Images/Shown/Doors/Portal.png"),
                       "tutorialEntrance": pygame.image.load("Images/Shown/Doors/TutDoor.png"),
                       "tutorialExit": pygame.image.load("Images/Shown/Doors/TutDoor.png"),
                       "cactus": pygame.transform.scale(pygame.image.load("Images/Shown/IntObstacles/Cactus.png"), scale3),
                       "bush": pygame.transform.scale(pygame.image.load("Images/Shown/IntObstacles/Bush.png"), scale4),
                       "bushClear": pygame.transform.scale(pygame.image.load("Images/Shown/IntObstacles/BushClear.png"), scale4)}
        
        self.kind = appearance
        self.image = self.images[self.kind]
        self.rect = self.image.get_rect(center = pos)
        
    def playerCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if self.kind == "bush":
                            self.kind = "bushClear"
                    elif self.kind == "bushClear":
                        self.kind = "bush"
                elif self.kind == "bushClear":
                    self.kind = "bush"
            elif self.kind == "bushClear":
                self.kind = "bush"
        elif self.kind == "bushClear":
            self.kind = "bush"
        self.image = self.images[self.kind]
    def update(self):
        pass
