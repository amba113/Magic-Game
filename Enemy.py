import pygame, sys, math, random

class Enemy():
    def __init__(self, startPos = [0, 0], kind = 1, speed = [0,0]):
        
        self.images = [pygame.image.load("Images/Enemy1.png")]
        
        self.kind = kind
        
        self.image = self.images[self.kind - 1]
        self.rect = self.image.get_rect(center = startPos)
        
        self.speedx = speed[0]
        self.speedy = speed[1]
        
        if self.kind == 1:
            self.hp = 100
            self.speedx = 2
            self.speedy = 0
            
        self.didHitX = False
        self.didHitY = False
        
        self.living = True
        
    def weaponCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if other.kind == "basic":
                            self.hp -= 5
                            print("Damage dealt, new health:", self.hp)
            
    def update(self, size):
        self.move()
        
        self.didHitX = False
        self.didHitY = False
        
        if self.hp < 0:
            self.hp = 0
        if self.hp == 0:
            self.living = False
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
                
    def wallTileCollide (self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.speedy = -self.speedy
                        self.speedx = -self.speedx
                        return True
        return False
