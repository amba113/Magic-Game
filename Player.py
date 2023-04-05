import pygame, sys, math, random, inspect
from Spells import *
from Sprite import *

class Player():
   
    def __init__(self, speed = 4, startPos = [0,0]):
       
        self.colorChoice = 0
        self.hatChoice = 0
        self.eyeChoice = 0
        self.mouthChoice = 0
        self.glassesChoice = 0
        self.shirtChoice = 0
        
        self.colors = ["Cyan", "Magenta", "Green", "Peach"]
        
        self.sprites = SpriteSheet("Images/" + self.colors[self.colorChoice] + " Spritesheet.png")
        self.hats = SpriteSheet("Images/Hat Spritesheet.png")
        self.eyes = SpriteSheet("Images/Eye Spritesheet.png")
        self.mouths = SpriteSheet("Images/Mouth Spritesheet.png")
        self.glasses = SpriteSheet("Images/Glass Spritesheet.png")
        self.shirts = SpriteSheet("Images/Shirt Spritesheet.png")
        
        self.images = self.sprites.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
        self.hat = self.hats.load_stripH([0, 0, 36, 90], 5,  (221, 255, 0))
        self.eye = self.eyes.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
        self.mouth = self.mouths.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
        self.glass = self.glasses.load_stripH([0, 0, 36, 90], 5,  (221, 255, 0))
        self.shirt = self.shirts.load_stripH([0, 0, 36, 90], 3,  (221, 255, 0))
        
        for i in self.images:
            i.blit(self.eye[self.eyeChoice], (0,0))
            i.blit(self.mouth[self.mouthChoice], (0,0)) 
            i.blit(self.glass[self.glassesChoice], (0,0))
            i.blit(self.hat[self.hatChoice], (0,0))
            i.blit(self.shirt[self.shirtChoice], (0,0))
        
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.Timer = 0
        self.TimerMax = 60/10
        
        self.sprinting = False
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
        self.hpTimer = 0
        self.hpHeal = False
        
        self.inventory = {"wand": None,
                          "halfHealPotion": 0,
                          "fullHealPotion": 0,
                          "speedPotion": 0,
                          "revivePotion": 0,
                          "healthPotion": 0,
                          "coins": 0,
                          "pets": [],
                          "spells": ["basic"]}
        
        self.counter = 0
        self.stop = 30
        self.dead = False
        self.roam = False
        
        self.hidden = False
        
    def update(self, size):
        if self.sprinting and not self.zoom:
            self.moveType = "sprint"
        elif self.sprinting and self.zoom:
            self.moveType = "zoomSprint"
        elif not self.sprinting and self.zoom:
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
        
        self.sprites = SpriteSheet("Images/" + self.colors[self.colorChoice] + " Spritesheet.png")
        
        if self.speedx < 0:
            self.speedx = -self.maxSpeed
            self.images = self.sprites.load_stripH([0, 90*2, 36, 90], 8,  (221, 255, 0))
            self.hat = self.hats.load_stripH([0, 90*2, 36, 90], 5,  (221, 255, 0))
            self.eye = self.eyes.load_stripH([0, 90*2, 36, 90], 8,  (221, 255, 0))
            self.mouth = self.mouths.load_stripH([0, 90*2, 36, 90], 8,  (221, 255, 0))
            self.glass = self.glasses.load_stripH([0, 90*2, 36, 90], 5,  (221, 255, 0))
            self.shirt = self.shirts.load_stripH([0, 90*2, 36, 90], 3,  (221, 255, 0))
            for i in self.images:
                i.blit(self.eye[self.eyeChoice], (0,0))
                i.blit(self.mouth[self.mouthChoice], (0,0)) 
                i.blit(self.glass[self.glassesChoice], (0,0))
                i.blit(self.hat[self.hatChoice], (0,0))
                i.blit(self.shirt[self.shirtChoice], (0,0))
        elif self.speedx > 0:
            self.speedx = self.maxSpeed
            self.images = self.sprites.load_stripH([0, 90*3, 36, 90], 8,  (221, 255, 0))
            self.hat = self.hats.load_stripH([0, 90*3, 36, 90], 5,  (221, 255, 0))
            self.eye = self.eyes.load_stripH([0, 90*3, 36, 90], 8,  (221, 255, 0))
            self.mouth = self.mouths.load_stripH([0, 90*3, 36, 90], 8,  (221, 255, 0))
            self.glass = self.glasses.load_stripH([0, 90*3, 36, 90], 5,  (221, 255, 0))
            self.shirt = self.shirts.load_stripH([0, 90*3, 36, 90], 3,  (221, 255, 0))
            for i in self.images:
                i.blit(self.eye[self.eyeChoice], (0,0))
                i.blit(self.mouth[self.mouthChoice], (0,0)) 
                i.blit(self.glass[self.glassesChoice], (0,0))
                i.blit(self.hat[self.hatChoice], (0,0))
                i.blit(self.shirt[self.shirtChoice], (0,0))
        if self.speedy < 0:
            self.speedy = -self.maxSpeed
            self.images = self.sprites.load_stripH([0, 90, 36, 90], 8,  (221, 255, 0))
            self.hat = self.hats.load_stripH([0, 90, 36, 90], 5,  (221, 255, 0))
            self.eye = self.eyes.load_stripH([0, 90, 36, 90], 8,  (221, 255, 0))
            self.mouth = self.mouths.load_stripH([0, 90, 36, 90], 8,  (221, 255, 0))
            self.glass = self.glasses.load_stripH([0, 90, 36, 90], 5,  (221, 255, 0))
            self.shirt = self.shirts.load_stripH([0, 90, 36, 90], 3,  (221, 255, 0))
            for i in self.images:
                i.blit(self.eye[self.eyeChoice], (0,0))
                i.blit(self.mouth[self.mouthChoice], (0,0)) 
                i.blit(self.glass[self.glassesChoice], (0,0))
                i.blit(self.hat[self.hatChoice], (0,0))
                i.blit(self.shirt[self.shirtChoice], (0,0))
        elif self.speedy > 0:
            self.speedy = self.maxSpeed
            self.images = self.sprites.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
            self.hat = self.hats.load_stripH([0, 0, 36, 90], 5,  (221, 255, 0))
            self.eye = self.eyes.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
            self.mouth = self.mouths.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
            self.glass = self.glasses.load_stripH([0, 0, 36, 90], 5,  (221, 255, 0))
            self.shirt = self.shirts.load_stripH([0, 0, 36, 90], 3,  (221, 255, 0))
            for i in self.images:
                i.blit(self.eye[self.eyeChoice], (0,0))
                i.blit(self.mouth[self.mouthChoice], (0,0)) 
                i.blit(self.glass[self.glassesChoice], (0,0))
                i.blit(self.hat[self.hatChoice], (0,0))
                i.blit(self.shirt[self.shirtChoice], (0,0))
        if self.speedx == 0 and self.speedy == 0:
            self.frame = -1
            self.images = self.sprites.load_stripH([0, 0, 36, 90], 1, (221, 255, 0))
            self.hat = self.hats.load_stripH([0, 0, 36, 90], 5, (221, 255, 0))
            self.eye = self.eyes.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
            self.mouth = self.mouths.load_stripH([0, 0, 36, 90], 8,  (221, 255, 0))
            self.glass = self.glasses.load_stripH([0, 0, 36, 90], 5,  (221, 255, 0))
            self.shirt = self.shirts.load_stripH([0, 0, 36, 90], 3,  (221, 255, 0))
            for i in self.images:
                i.blit(self.eye[self.eyeChoice], (0,0))
                i.blit(self.mouth[self.mouthChoice], (0,0)) 
                i.blit(self.glass[self.glassesChoice], (0,0))
                i.blit(self.hat[self.hatChoice], (0,0))
                i.blit(self.shirt[self.shirtChoice], (0,0))
        
        self.move()
        self.wallCollide(size)
        
        self.didHitX = False
        self.didHitY = False
                
        if self.counter < 300:
            self.counter += 1
        else:
            self.counter = 0
            self.zoom = False
        if self.hp > 0:
            self.roam = False
            if self.hpHeal == True and self.hpTimer == (60*3) and self.hp < self.hpMax:
                self.hp += 5
                self.hpTimer = 0
                if self.hp > self.hpMax:
                    self.hp = self.hpMax
                print("Healed")
            elif self.hpHeal:
                self.hpTimer += 1

        if self.hp < 0:
            self.hp = 0
        
        if self.hp == 0:
            self.speed = [0, 0]
            self.kind = "dead"
            self.inventory["speedPotion"] = 0
            self.inventory["halfHealPotion"] = 0
            self.inventory["fullHealPotion"] = 0
            self.inventory["healthPotion"] = 0
            self.hpMax = 100
            self.dead = True
        
        if self.inventory["wand"] != None and self.dead == False:
            self.kind = str(self.inventory["wand"]) + "Wand"
        
        self.Timer += 1
        self.animate()
    
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
                
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if other.kind == "cactus":
                            if self.counter % 10 == 0:
                                self.hp -= 1
                        else:
                            diffx = abs(self.rect.centerx-other.rect.centerx)
                            diffy = abs(self.rect.centery-other.rect.centery)
                            if diffx > diffy:
                                if self.rect.centerx > other.rect.centerx:
                                    self.rect.left = other.rect.right + .5
                                elif self.rect.centerx < other.rect.centerx:
                                    self.rect.right = other.rect.left - .5
                            else:
                                if self.rect.centery > other.rect.centery:
                                    self.rect.top = other.rect.bottom + .5
                                elif self.rect.centery < other.rect.centery:
                                    self.rect.bottom = other.rect.top - .5
                            

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
                        elif other.kind == "tutorialEntrance":
                            self.coord = [.5, -1]
                            self.prevCoord = [1, 0]
                        elif other.kind == "tutorialExit":
                            self.coord = [0, 0]
                            self.prevCoord = [.5, -1]
                        elif other.kind == "top":
                            self.prevCoord = self.coord.copy()
                            self.coord[1] -= 1
                        elif other.kind == "bottom":
                            self.prevCoord = self.coord.copy()
                            self.coord[1] += 1
                        elif other.kind == "left":
                            self.prevCoord = self.coord.copy()
                            self.coord[0] -= 1
                        elif other.kind == "right":
                            self.prevCoord = self.coord.copy()
                            self.coord[0] += 1 
                                
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
                                print("wand acquired")
                            elif other.kind == "halfHealPotion":
                                self.inventory["halfHealPotion"] += 1
                            elif other.kind == "fullHealPotion":
                                self.inventory["fullHealPotion"] += 1
                            elif other.kind == "speedPotion":
                                self.inventory["speedPotion"] += 1
                            elif other.kind == "revivePotion":
                                self.inventory["revivePotion"] += 1
                            elif other.kind == "healthPotion":
                                self.inventory["healthPotion"] += 1
                            elif other.kind == "basic2Spell":
                                self.inventory["spells"] += ["basic2"]
                            elif other.kind == "singleCoin":
                                self.inventory["coins"] += 1
                                print("Bank balance: ", self.inventory["coins"])
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
                                if other.kind == "basic":
                                    self.hp -= 5
                                if other.kind == "strong":
                                    self.hp -= 10
                                if other.kind == "bee":
                                    self.hp -= 3
    def hideCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.hidden = True
        else:
            self.hidden = False
            
    def purchase(self, selection, kind):
        if kind.lower() == "pet":
            if selection == "blackCat":
                if self.inventory["coins"] >= 3:
                    self.inventory["coins"] -= 3
                    self.inventory["pets"] += ["blackCat"]
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
            elif selection == "calicoCat":
                if self.inventory["coins"] >= 1:
                    self.inventory["coins"] -= 1
                    self.inventory["pets"] += ["calicoCat"]
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
            elif selection == "owl":
                if self.inventory["coins"] >= 2:
                    self.inventory["coins"] -= 2
                    self.inventory["pets"] += ["owl"]
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
            elif selection == "frog":
                if self.inventory["coins"] >= 5:
                    self.inventory["coins"] -= 5
                    self.inventory["pets"] += ["frog"]
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
        elif kind.lower() == "spell":
            pass
        elif kind.lower() == "potion":
            if selection == "speed":
                if self.inventory["coins"] >= 1:
                    self.inventory["coins"] -= 1
                    self.inventory["speedPotion"] += 1
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
            elif selection == "health":
                if self.inventory["coins"] >= 2:
                    self.inventory["coins"] -= 2
                    self.inventory["healthPotion"] += 1
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
            elif selection == "fullHeal":
                if self.inventory["coins"] >= 3:
                    self.inventory["coins"] -= 3
                    self.inventory["fullHealPotion"] += 1
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
            elif selection == "halfHeal":
                if self.inventory["coins"] >= 1:
                    self.inventory["coins"] -= 1
                    self.inventory["halfHealPotion"] += 1
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
            elif selection == "revive":
                if self.inventory["coins"] >= 10:
                    self.inventory["coins"] -= 10
                    self.inventory["revivePotion"] += 1
                    return True
                else:
                    print("You are too poor to afford this")
                    return False
        elif kind.lower() == "clothing":
            pass

    def animate(self):
        if self.Timer >= self.TimerMax:
            self.Timer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]
