import pygame, sys, math, random

class Obstacle():

    def __init__(self, pos = [25,25], appearance = "wall"):
        
        self.appearance = appearance
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
        elif appearance == "top" or appearance == "bottom":
            self.num = 2
        elif appearance == "left" or appearance == "right":
            self.num = 3
        
        self.kind = appearance
        self.image = self.images[self.num]
        self.rect = self.image.get_rect(center = pos)
        
    def update(self):
        pass
    # ~ def playerCollide(self, other):
        # ~ if self.rect.right > other.rect.left:
            # ~ if self.rect.left < other.rect.right:
                # ~ if self.rect.bottom > other.rect.top:
                    # ~ if self.rect.top < other.rect.bottom:
                        # ~ if self.kind == "wall" or self.kind == "tree":
                            # ~ pass
                        # ~ else:
                            # ~ if self.kind == "top":
                                  # ~ coord[1] -= 1
                            # ~ elif self.kind == "bottom":
                                  # ~ coord[1] += 1
                            # ~ elif self.kind == "left":
                                  # ~ coord[0] -= 1
                            # ~ elif self.kind == "right":
                                  # ~ coord[0] += 1
                        # ~ print("New room: " + str(coord[1]) + str(coord[0]))
            
