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
            self.spdx = 2
            self.spdy = 0
            self.vel = 2
            
        self.didHitX = False
        self.didHitY = False
        
        self.living = True
        self.angry = False
        
        self.counter = 0
        self.stop = 30
        
        self.xpos = startPos[0]
        self.ypos = startPos[1]
        
    def weaponCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if other.kind == "basic":
                            self.hp -= 5
                            print("Damage dealt, new health:", self.hp)
                        self.angry = True
                        self.counter = 0
                        return True
        return False
            
    def update(self, playerPos, size):
        
        self.spdy = self.speedy
        self.spdx = self.speedx
        
        if self.angry:
            self.attack(playerPos)
            if self.counter < 200:
                self.counter += 1
            else:
                self.counter = 0
                self.angry = False
                
                self.speedx = self.spdx
                self.speedy = self.spdy
        else:
            if (self.speedx < 2 and self.speedx > -2) and (self.speedy < 0 or self.speedy > 0):
                self.speedx = 2
                self.speedy = 0

        self.move()
        
        self.wallCollide(size)
        
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
                        self.spdy = self.speedy
                        self.spdx = self.speedx
                        return True
        return False
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didHitY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didHitY = True
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.didHitY = True
        if not self.didHitX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.didHitX = True
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.didHitX = True
    # ~ def wallTileCollide (self, other):
        # ~ if self.rect.right > other.rect.left:
            # ~ if self.rect.left < other.rect.right:
                # ~ if self.rect.bottom > other.rect.top:
                    # ~ if self.rect.top < other.rect.bottom:
                        # ~ self.speedy = -self.speedy
                        # ~ self.speedx = -self.speedx
                        # ~ self.spdy = self.speedy
                        # ~ self.spdx = self.speedx
                        # ~ return True
        # ~ return False
        
    def attack(self, target):
        self.xpos = self.rect.centerx
        self.ypos = self.rect.centery
        
        self.x = target[0] - self.rect.centerx
        self.y = target[1] - self.rect.centery
        
        self.angle = math.atan2(self.y, self.x)
        self.speedx = self.vel * math.cos(self.angle)
        self.speedy = self.vel * math.sin(self.angle)

        self.xpos += self.speedx
        self.ypos += self.speedy
        self.pos = [self.xpos, self.ypos]
        self.rect.center = [self.xpos, self.ypos]

