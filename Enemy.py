import pygame, sys, math, random

class Enemy():
    def __init__(self, startPos = [0, 0], kind = 1):
        
        self.images = [pygame.image.load("Images/Enemy1.png")]
        
        self.kind = kind
        
        self.image = self.images[self.kind - 1]
        self.rect = self.image.get_rect(center = startPos)
        
        
        if self.kind == 1:
            self.hp = 100
            self.speed = [2, 0]
        
    def weaponCollide(self, other):
        if other.kind == "spell":
            self.hp -= 5
            
    def update(self):
        self.move()
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.speedx = -self.speedx
                        self.speedy = -self.speedy
                        return True
        return False
