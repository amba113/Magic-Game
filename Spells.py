import pygame, sys, math

class Spell():
    def __init__(self, spell, startPos, target):
        self.images = [pygame.image.load("Images/SpellTest.png")]
        
        self.kind = spell
        
        if self.kind == "basic":
            self.num = 0
            self.vel = 2
        
        self.x = target[0] - startPos[0]
        self.y = target[1] - startPos[0]
        
        self.angle = math.atan(self.y/self.x)
        
        self.xspeed = self.vel * math.cos(self.angle)
        self.yspeed = self.vel * math.sin(self.angle)
        
        self.image = self.images[self.num]
        
        self.rect = self.image.get_rect(center = startPos)
        
        
        self.speedx = self.xspeed
        self.speedy = self.yspeed
        self.speed = [self.speedx, self.speedy]
        self.living = True
        
    def update(self):
        self.move()
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.living = False
                        speed = [0, 0]
                        return True
        return False
        
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.living = False
                        speed = [0, 0]
                        return True
        return False
