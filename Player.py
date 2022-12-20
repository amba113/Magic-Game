import pygame, sys, math, random
from Spells import *

class Player():
   
    
    
    def __init__(self, speed = 2, startPos = [0,0]):
        
        scale = [60, 60]
        self.images = [pygame.transform.scale(pygame.image.load("Images/Person 1.png"), scale),
                       pygame.transform.scale(pygame.image.load("Images/PersonWand1.png"), scale),
                       pygame.transform.scale(pygame.image.load("Images/PersonWand2.png"), scale),
                       pygame.transform.scale(pygame.image.load("Images/Dead Person.png"), scale)]

        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        
        self.wandFrame = 1
        
        self.rect = self.image.get_rect(center = startPos)
        
        self.speed = [0,0]
        self.speedx = self.speed[0]
        self.speedy = self.speed[1]
        self.speed = [self.speedx, self.speedy]
        self.walkSpeed = speed
        self.sprintSpeed = speed*2
        self.zoomSpeed = speed * 3
        self.zoomSprintSpeed = speed * 5
        self.maxSpeed = self.walkSpeed
        self.moveType = "walk"
        self.zoom = False
        
        self.coord = [1, 1]
        self.prevCoord = [1,1]
        
        self.didHitX = False
        self.didHitY = False
        
        self.hp = 100
        self.hpMax = 100
        
        self.inventory = {"wand": None,
                          "halfHealPotion": 0,
                          "fullHealPotion": 0,
                          "speedPotion": 0,
                          "revivePotion": 0,
                          "healthPotion": 0
        }
        self.spells = ["basic"]
        
        self.counter = 0
        self.stop = 30
        self.dead = False
        
    def update(self, size):
        self.move()
        self.wallCollide(size)
        
        self.didHitX = False
        self.didHitY = False
        
        self.image = self.images[self.frame]
        
        if self.counter < 150:
            self.counter += 1
        else:
            self.counter = 0
            self.zoom = False
            
        if self.hp < 0:
            self.hp = 0
        
        if self.hp == 0:
            print("You dead")
            self.speed = [0, 0]
            self.frame = 3
            self.inventory["speedPotion"] = 0
            self.inventory["halfHealPotion"] = 0
            self.inventory["fullHealPotion"] = 0
            self.inventory["healthPotion"] = 0
            self.hpMax = 100
            self.dead = True
    
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
    
    def goto(self, pos):
        self.rect.center = pos

    def shoot(self, spell, posM):
        return Spell(spell, self.rect.center, posM)
        
    def goKey(self, direction):
        if self.zoom:
            self.maxSpeed = self.maxSpeed * 5
        
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
   
    def sprint(self, sprinting):
        if sprinting and self.moveType != "zoom":
            self.moveType = "sprint"
        elif sprinting and self.moveType == "zoom":
            self.moveType = "zoomSprint"
        elif not sprinting and self.moveType == "zoom":
            self.moveType = "zoom"
        else:
            self.moveType = "walk"
            
        
        if self.moveType == "sprint":
            self.maxSpeed = self.sprintSpeed
        elif self.moveType == "zoom":
            self.maxSpeed = self.zoomSpeed
        elif self.moveType == "zoomSprint":
            self.maxSpeed = self.zoomSprintSpeed
        else:
            self.maxSpeed = self.walkSpeed
    
            
        if self.speedx < 0:
            self.speedx = -self.maxSpeed
        elif self.speedx > 0:
            self.speedx = self.maxSpeed
        if self.speedy < 0:
            self.speedy = -self.maxSpeed
        elif self.speedy > 0:
            self.speedy = self.maxSpeed
                
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if other.kind == "cactus":
                            if self.counter % 10 == 0:
                                self.hp -= 1
                        else:
                            self.speedx = -self.speedx
                            self.speedy = -self.speedy
                            self.move()
                            
                            self.speedx = 0
                            self.speedy = 0
                            
                            self.move()

                        return True
        return False

    def doorCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.speedx = -self.speedx
                        self.speedy = -self.speedy
                        self.move()
                        
                        self.speedx = 0
                        self.speedy = 0
                        
                        self.move()
                        

                        if other.kind == "wall" or other.kind == "tree":
                            pass
                        elif other.kind == "portal1":
                            self.coord = [0, 2]
                            self.prevCoord = [3, 0]
                        elif other.kind == "portal2":
                            self.coord = [3, 0]
                            self.prevCoord = [0, 2]
                        elif other.kind == "tutent":
                            self.coord = [.5, -1]
                            self.prevCoord = [1, 0]
                        elif other.kind == "tutext":
                            self.coord = [0, 0]
                            self.prevCoord = [.5, -1]
                        else:
                            if other.kind == "top":
                                self.coord[1] = self.coord[1] - 1
                                self.prevCoord[1] = self.coord[1] + 1
                            elif other.kind == "bottom":
                                self.coord[1] = self.coord[1] + 1
                                self.prevCoord[1] = self.coord[1] - 1
                            elif other.kind == "left":
                                self.coord[0] = self.coord[0] - 1
                                self.prevCoord[0] = self.coord[0] + 1
                            elif other.kind == "right":
                                self.coord[0] = self.coord[0] + 1
                                self.prevCoord[0] = self.coord[0] - 1
                                
                        self.speedx = 0
                        self.speedy = 0
                        
                        self.move()
                        return True
        return False
        
    def itemCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if self.dead == False:
                            if other.kind == "wand":
                                self.inventory["wand"] = other
                                self.wandFrame = other.num + 1
                                self.frame = self.wandFrame
                            elif other.kind == "halfPotion":
                                self.inventory["halfHealPotion"] += 1
                            elif other.kind == "fullPotion":
                                self.inventory["fullHealPotion"] += 1
                            elif other.kind == "speedPotion":
                                self.inventory["speedPotion"] += 1
                            elif other.kind == "revivePotion":
                                self.inventory["revivePotion"] += 1
                            elif other.kind == "healthPotion":
                                self.inventory["healthPotion"] += 1
                            elif other.kind == "Spell2":
                                self.spells += ["basic2"]
                            else:
                                pass
                            return True
        return False

    def useItem(self, key):
        if key == "f":
            if self.inventory["fullHealPotion"] > 0 and self.hp > 0:
                self.hp = self.hpMax
                self.inventory["fullHealPotion"] -= 1
            else:
                print("No full heals left")
        if key == "h":
            if self.inventory["halfHealPotion"] > 0 and self.hp > 0:
                self.half = (self.hpMax-self.hp)/2
                self.hp += self.half
                self.inventory["halfHealPotion"] -= 1
            else:
                print("No half heals left")
        if key == "g":
            if self.inventory["speedPotion"] > 0:
                self.counter = 0
                self.zoom = True
                self.inventory["speedPotion"] -= 1
            else:
                print("No speeds left")
        if key == "v":
            if self.inventory["revivePotion"] > 0:
                if self.hp == 0:
                    self.hp = self.hpMax
                    self.inventory["revivePotion"] -= 1
                    self.dead = False
                    if self.inventory["wand"] == None:
                        self.frame = 0
                    else:
                        self.frame = self.wandFrame
                else:
                    print("Dude, live your life...you ain't dead yet")
            else:
                print("No revives left")
        if key == "t":
            if self.inventory["healthPotion"] > 0:
                self.hpMax += 10
                self.inventory["healthPotion"] -= 1
            else:
                print("No healths left")
                
    def enemyCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if self.dead == False:
                            if self.counter % 20 == 0:
                                if other.kind == 1:
                                    self.hp -= 5
                                if other.kind == 2:
                                    self.hp -= 10
