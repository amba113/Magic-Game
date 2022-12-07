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
        
    def weaponCollide(self, other):
        if other.kind == "spell":
            self.hp -= 5
            
    def update(self, size):
        self.move()
        self.wallCollide(size)
        
        self.didHitX = False
        self.didHitY = False
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def wallCollide(self, size):
        width = size[0] - 50
        height = size[1] - 50
        if not self.didHitY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didHitY = True
            if self.rect.top < 50:
                self.speedy = -self.speedy
                self.didHitY = True
        if not self.didHitX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.didHitX = True
            if self.rect.left < 50:
                self.speedx = -self.speedx
                self.didHitX = True
