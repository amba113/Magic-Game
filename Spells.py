import pygame, sys, math

class Spell():
    def __init__(self, spell, startPos, target):
        self.images = {"basic1": pygame.image.load("Images/Shown/Spells/SpellTest.png"), 
                       "basic2": pygame.image.load("Images/Shown/Spells/SpellTest2.png")}
        
        self.kind = spell
        
        if self.kind == "basic1":
            self.vel = 2
        if self.kind == "basic2":
            self.vel = 4
        
        self.x = target[0] - startPos[0]
        self.y = target[1] - startPos[1]
        
        self.angle = math.atan2(self.y, self.x)
        self.xspeed = self.vel * math.cos(self.angle)
        self.yspeed = self.vel * math.sin(self.angle)
        
        self.image = self.images[self.kind]
        
        self.rect = self.image.get_rect(center = startPos)
        self.xpos = startPos[0]
        self.ypos = startPos[1]
        self.pos = [self.xpos, self.ypos]
        
        self.speed = [self.xspeed, self.yspeed]
        self.living = True
        
    def update(self):
        self.move()
        
    def move(self):
        self.speed = [self.xspeed, self.yspeed]
        self.xpos += self.xspeed
        self.ypos += self.yspeed
        self.pos = [self.xpos, self.ypos]
        self.rect.center = [int(self.xpos), int(self.ypos)]
        
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
