import pygame, sys, math

class Spell():
    def __init__(self, spell, startPos, target):
        self.images = {"basic": pygame.image.load("Images/Shown/Spells/Spell 1.png"), 
                       "speed": pygame.image.load("Images/Shown/Spells/Spell 2.png"), 
                       "power": pygame.image.load("Images/Shown/Spells/Spell 3.png"), 
                       "spdpower": pygame.image.load("Images/Shown/Spells/Spell 4.png"), 
                       "speed+": pygame.image.load("Images/Shown/Spells/Spell 5.png"), 
                       "spdpower+": pygame.image.load("Images/Shown/Spells/Spell 6.png"), 
                       "power+": pygame.image.load("Images/Shown/Spells/Spell 7.png"), 
                       "spd+power": pygame.image.load("Images/Shown/Spells/Spell 8.png"),
                       "spd+power+": pygame.image.load("Images/Shown/Spells/Spell 9.png")}
        
        self.kind = spell
        
        if self.kind == "basic":
            self.vel = 2
        elif self.kind == "speed":
            self.vel = 4
        elif self.kind == "power":
            self.vel = 2
        elif self.kind == "spdpower":
            self.vel = 4
        elif self.kind == "speed+":
            self.vel = 6
        elif self.kind == "spdpower+":
            self.vel = 4
        elif self.kind == "power+":
            self.vel = 2
        elif self.kind == "spd+power":
            self.vel = 6
        elif self.kind == "spd+power+":
            self.vel = 6
        
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
