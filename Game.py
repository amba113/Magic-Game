import pygame, sys, math, random, os
from Player import *
from MapLoader import *
from Obstacles import *
from Items import *
from Enemy import *
from Text import *
from Text2 import *
from Spells import *

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

counter = 0

health = Text("HP: ", [5,10])
speedPotions = Text("Speed Potions: ", [900-170, 2], 24)
fullPotions = Text("Full Heal Potions: ", [900-170, 17], 24)
halfPotions = Text("Half Heal Potions: ", [900-170, 32], 24)
revivePotions = Text("Revive Potions: ", [900-170, 700-20], 24)
healthPotions = Text("Health Potions: ", [900-170, 700-35], 24)
position = Text("X,Y: ", [5, 700-20], 24)

deathNote1 = Text2("You have no revive potions...you dead XD", [900/2, 700/2], 36)
deathNote2 = Text2("Press V to revive", [900/2, 700/2], 36)

tiles = loadMap()
walls = tiles[0]
doors = tiles[1]
hides = tiles[5]
player = Player(2, tiles[2])
players = [player]
items = tiles[3]
enemies = tiles[4]
spells = []
spellType = "basic"

loc = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            direct = "Rooms/Sav/"
            files = os.listdir(direct)
            for f in files:
                if f[-4:] == ".sav":
                    
                    os.remove("Rooms/Sav/" + f)
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player.sprint(True)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player.sprint(False)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                player.useItem("f")
            elif event.key == pygame.K_h:
                player.useItem("h")
            elif event.key == pygame.K_g:
                player.useItem("g")
            elif event.key == pygame.K_v:
                if player.dead:
                    player.goto(tiles[2])
                player.useItem("v")
                for enemy in enemies:
                    enemy.angry = False
            elif event.key == pygame.K_t:
                player.useItem("t")
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player.goto(tiles[2])
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and event.key == pygame.KMOD_CTRL:
                item.wandChoice(1)
            elif event.key == pygame.K_2 and event.key == pygame.KMOD_CTRL:
                item.wandChoice(2)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                spellType = "basic"
            elif event.key == pygame.K_2:
                if "basic2" in player.spells:
                    spellType = "basic2"
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            statesM = pygame.mouse.get_pressed(num_buttons = 3)
            if statesM[0]:
                posM = pygame.mouse.get_pos()
                spells += [player.shoot(spellType, posM)]
                
    for wall in walls:
        player.wallTileCollide(wall)
    
    for item in items:
        if player.itemCollide(item):
            items.remove(item)
            
    for enemy in enemies:
        player.enemyCollide(enemy)
        
    for player in players:
        enemy.playerSense(player)
        
    for wall in walls:
        enemy.wallTileCollide(wall)
    
    for wall in walls:
        for spell in spells:
            spell.wallTileCollide(wall)
    for enemy in enemies:
        for spell in spells:
            spell.collide(enemy)
            
    for spell in spells:
        enemy.weaponCollide(spell)
    
    for hide in hides:
        player.hideCollide(hide)
        
    for hide in hides:
        enemy.hideCollide(hide)
        
    for player in players:
        hide.playerCollide(player)
    
    player.update(size)
    enemy.update(player.rect.center, size, player.hidden)
    for spell in spells:
        spell.update()
    
    health.update(str(player.hp) + "/" + str(player.hpMax))
    position.update(str(player.coord[0]) + "," + str(player.coord[1]))
    
    speedPotions.update(player.inventory["speedPotion"])
    fullPotions.update(player.inventory["fullHealPotion"])
    halfPotions.update(player.inventory["halfHealPotion"])
    revivePotions.update(player.inventory["revivePotion"])
    healthPotions.update(player.inventory["healthPotion"])
    
    deathNote1.update("")
    deathNote2.update("")
    
    for door in doors:
        if player.doorCollide(door):
            saveMap(items, enemies, player.prevCoord)
            
            loc = door.kind
            tiles = loadMap(player.coord, loc)
            
            walls = tiles[0]
            doors = tiles[1]
            items = tiles[3]
            enemies = tiles[4]
            hides = tiles[5]
            
            player.goto(tiles[2]) #relocate player

    screen.fill((250, 175, 225))
    
    
            
    for spell in spells:
        if not spell.living:
            spells.remove(spell)
            
    for enemy in enemies:
        if not enemy.living:
            enemies.remove(enemy)


    if player.dead:
        if player.inventory["revivePotion"] > 0:
            screen.blit(deathNote2.image, deathNote2.rect)
        elif player.inventory["revivePotion"] == 0:
            screen.blit(deathNote1.image, deathNote1.rect)
    else:
        for item in items:
            screen.blit(item.image, item.rect)
        for spell in spells:
            screen.blit(spell.image, spell.rect)
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        for enemy in enemies:
            screen.blit(enemy.image, enemy.rect)
        for door in doors:
            screen.blit(door.image, door.rect)
        screen.blit(player.image, player.rect)
        for hide in hides:
            screen.blit(hide.image, hide.rect)
        screen.blit(health.image, health.rect)
        screen.blit(speedPotions.image, speedPotions.rect)
        screen.blit(fullPotions.image, fullPotions.rect)
        screen.blit(halfPotions.image, halfPotions.rect)
        screen.blit(revivePotions.image, revivePotions.rect)
        screen.blit(healthPotions.image, healthPotions.rect)
        screen.blit(position.image, position.rect)

    pygame.display.flip()
    clock.tick(60)
