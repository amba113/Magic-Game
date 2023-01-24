import pygame, sys, math, random

class Pet():
    def __init__(self, startPos, kind = 1, vel = 2, speed = [0,0]):
        
        self.images = [pygame.image.load("Images/BlackCat.png"),
                       pygame.image.load("Images/CalicoCat.png"),
                       pygame.image.load("Images/Owl.png"),
                       pygame.image.load("Images/Frog.png")]
        
        self.kind = kind
        
        self.image = self.images[self.kind - 1]
        self.rect = self.image.get_rect(center = startPos)
        
        self.speedx = speed[0]
        self.speedy = speed[1]
        
        self.vel = vel

    def update(self, playerPos):
        self.move()
        self.follow(playerPos)
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def follow(self, target):
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
