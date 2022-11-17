import pygame, sys, math, random

class Player():
    def __init__(self, maxSpeed = 2, startPos = [0,0]):
        
        scale = [100, 100]
        self.images = [pygame.transform.scale(pygame.image.load("Images/Test Player.png"), scale)]

        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        
        
        self.rect = self.image.get_rect(center = startPos)
        
        self.speed = [0,0]
        self.speedx = self.speed[0]
        self.speedy = self.speed[1]
        self.speed = [self.speedx, self.speedy]
        self.maxSpeed = maxSpeed
        
        self.didHitX = False
        self.didHitY = False
        
    def update(self, size):
        self.move()
        self.wallCollide(size)
        
        self.didHitX = False
        self.didHitY = False
    
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
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def shoot(self):
        pass
        
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up":
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "sleft":
            if self.speedx < 0:
                self.speedx = 0
        elif direction == "sright":
            if self.speedx > 0:
                self.speedx = 0
        elif direction == "sup":
            if self.speedy < 0:
                self.speedy = 0
        elif direction == "sdown":
            if self.speedy > 0:
                self.speedy = 0
   
    def sprint(self, value):
        if value == True:
            self.speedx = self.speedx * 5
            self.speedy = self.speedy * 5
        elif value == False:
            if self.speedx < 0:
                self.speedx = -self.maxSpeed
            elif self.speedx > 0:
                self.speedx = self.maxSpeed
            else:
                self.speedx = 0
            if self.speedy < 0:
                self.speedy = -self.maxSpeed
            elif self.speedy > 0:
                self.speedy = self.maxSpeed
            else:
                self.speedy = 0
                
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.speedx = 0
                        self.speedy = 0
                        # ~ self.rect = self.rect.move([2,2])
                        # ~ self.speedx = 0
                        # ~ self.speedy = 0
                        xDist = abs(self.rect.centerx - other.rect.centerx)
                        yDist = abs(self.rect.centery - other.rect.centery)
                        self.move()

                        if xDist < yDist:
                            self.rect = self.rect.move([2,2])
                        if yDist < xDist:
                            self.rect = self.rect.move([-2,-2])
                        
                        return True
        return False
