import pygame, sys, math, random
from Spells import*

class Pet():
    def __init__(self, startPos, kind, vel = 2, speed = [0,0]):
        
        self.images = {"blackCat": pygame.image.load("Images/BlackCat.png"),
                       "calicoCat": pygame.image.load("Images/CalicoCat.png"),
                       "owl": pygame.image.load("Images/Owl.png"),
                       "frog": pygame.image.load("Images/Frog.png")}
        
        self.kind = kind
        
        self.image = self.images[self.kind]
        self.rect = self.image.get_rect(center = startPos)
        
        self.speedx = speed[0]
        self.speedy = speed[1]
        
        self.vel = vel

    def update(self, playerPos, status = False, enemyPos = [0,0]):
        if status == True:
            self.defend(enemyPos)
        else:
            self.move()
            self.follow(playerPos)
              
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def follow(self, target):
        adjustx = 25
        adjusty = 15
        self.xpos = self.rect.centerx
        self.ypos = self.rect.centery
        
        if self.rect.centerx < target[0]:
            adjustx = -30
        else:
            adjustx = 25
        
        
        self.x = target[0] + adjustx - self.rect.centerx
        self.y = target[1] + adjusty - self.rect.centery
        
        if self.x > 50 or self.y > 50 or self.x < -50 or self.y < -50:
            self.vel = 6
        else:
            self.vel = 2
        
        self.angle = math.atan2(self.y, self.x)
        self.speedx = self.vel * math.cos(self.angle)
        self.speedy = self.vel * math.sin(self.angle)

        self.xpos += self.speedx
        self.ypos += self.speedy
        self.pos = [self.xpos, self.ypos]
        self.rect.center = [self.xpos, self.ypos]
        
    def defend(self, target):
        self.vel = 4
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
        
    def goto(self, pos):
        self.rect.center = pos
