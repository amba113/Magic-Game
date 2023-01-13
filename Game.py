import pygame, sys, math, random, os
from Player import *
from MapLoader import *
from Obstacles import *
from Items import *
from Enemy import *
from Text import *
from Text2 import *
from Spells import *
from Popup import *
from WandButton import *
from SettingsButtons import *
from SettingsOpen import *

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

counter = 0

health = Text("HP: ", [55,10])
speedPotions = Text("Speed Potions: ", [900-170, 2], 24)
fullPotions = Text("Full Heal Potions: ", [900-170, 17], 24)
halfPotions = Text("Half Heal Potions: ", [900-170, 32], 24)
revivePotions = Text("Revive Potions: ", [900-170, 700-20], 24)
healthPotions = Text("Health Potions: ", [900-170, 700-35], 24)
position = Text("X,Y: ", [5, 700-20], 24)

deathNote1 = Text2("You have no revive potions...you dead XD", [900/2, 700/2], 36)
deathNote2 = Text2("Press V to revive", [900/2, 700/2], 36)
settingsOpen = SettingsOpen([25, 25])

tiles = loadMap()
walls = tiles[0]
doors = tiles[1]
hides = tiles[5]
player = Player(4, tiles[2])
players = [player]
items = tiles[3]
enemies = tiles[4]
spells = []
spellType = "basic"
selected = ""
popup = []
close = []

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
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player.sprinting = True
                
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

            if event.key == pygame.K_1:
                spellType = "basic"
            elif event.key == pygame.K_2:
                if "basic2" in player.spells:
                    spellType = "basic2"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player.sprinting = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            statesM = pygame.mouse.get_pressed(num_buttons = 3)
            posM = pygame.mouse.get_pos()
            if statesM[0]:
                if settingsOpen.click(posM):
                    selected = ""
                    setOpen = True
                    buttons = [SettingsButton([60, 65], 1),
                               SettingsButton([60, 115], 2),
                               SettingsButton([60, 165], 3)]
                    popup = []
                    while selected == "" and setOpen == True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                direct = "Rooms/Sav/"
                                files = os.listdir(direct)
                                for f in files:
                                    if f[-4:] == ".sav":
                                        
                                        os.remove("Rooms/Sav/" + f)
                                sys.exit();
                            
                            elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                    player.goKey("sleft")
                                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                    player.goKey("sright")
                                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                                    player.goKey("sup")
                                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                    player.goKey("sdown")
                                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                                    player.sprinting = False
                        
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    setOpen = False
                        
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                stateM = pygame.mouse.get_pressed(num_buttons = 3)
                                if stateM[0]:
                                    buttonClicked = False
                                    for button in buttons:
                                        if button.click(pygame.mouse.get_pos()):
                                            buttonClicked = True
                                            selected = button.kind
                                    if not buttonClicked:
                                        setOpen = False
                        if selected == len(buttons):
                            direct = "Rooms/Sav/"
                            files = os.listdir(direct)
                            for f in files:
                                if f[-4:] == ".sav":
                                    
                                    os.remove("Rooms/Sav/" + f)
                            sys.exit()
                        
                        for button in buttons:
                            screen.blit(button.image, button.rect)
                        if popup != []:
                            screen.blit(popup[0].image, popup[0].rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
                elif player.inventory["wand"] != None:
                    spells += [player.shoot(spellType, posM)]
    if selected == 2:
        popup = [Popup([size[0]/2, size[1]/2], 1)]
        close = [SettingsButton([775, 125], 4)]
        if statesM[0]:
            if close[0].click(pygame.mouse.get_pos()):
                print("x pressed")
                selected = ""
                
    
    for wall in walls:
        player.wallTileCollide(wall)
    
    for item in items:
        if player.itemCollide(item):
            if item.kind == "wand":
                selected = ""
                popup = Popup([size[0]/2, size[1]/2], 0)
                buttons = [WandButton([(size[0]/2)/2 + 40, (size[1]/2)], 1),
                           WandButton([(size[0]/2) - 60, (size[1]/2)], 2),
                           WandButton([(size[0]/2) + 60, (size[1]/2)], 3),
                           WandButton([3*(size[0]/2)/2 - 40, (size[1]/2)], 4)]
                while selected == "":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            direct = "Rooms/Sav/"
                            files = os.listdir(direct)
                            for f in files:
                                if f[-4:] == ".sav":
                                    
                                    os.remove("Rooms/Sav/" + f)
                            sys.exit();
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                direct = "Rooms/Sav/"
                                files = os.listdir(direct)
                                for f in files:
                                    if f[-4:] == ".sav":
                                        
                                        os.remove("Rooms/Sav/" + f)
                                sys.exit();
                        elif event.type == pygame.KEYUP:
                            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                player.goKey("sleft")
                            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                player.goKey("sright")
                            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                                player.goKey("sup")
                            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                player.goKey("sdown")
                            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                                player.sprinting = False
                            
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        stateM = pygame.mouse.get_pressed(num_buttons = 3)
                        if stateM[0]:
                            for button in buttons:
                                if button.click(pygame.mouse.get_pos()):
                                    selected = button.kind
                    print(selected)
                    

                    screen.blit(popup.image, popup.rect)
                    for button in buttons:
                        screen.blit(button.image, button.rect)
                    pygame.display.flip()
                    clock.tick(60)
                player.wandFrame = selected
                player.frame = player.wandFrame
                        
            items.remove(item)
            
    for enemy in enemies:
        player.enemyCollide(enemy)
        enemy.playerSense(player)
        
        for wall in walls:
            enemy.wallTileCollide(wall)
        for hide in hides:
            enemy.hideCollide(hide)
        for spell in spells:
            spell.collide(enemy)
            enemy.weaponCollide(spell)
        enemy.update(player.rect.center, size, player.hidden)
        
    for wall in walls:
        for spell in spells:
            spell.wallTileCollide(wall)        
    
    for hide in hides:
        player.hideCollide(hide)
        hide.playerCollide(player)
    
    player.update(size)
    
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
            print("prev:", player.prevCoord, door.kind)
            loc = door.kind
            tiles = loadMap(player.coord, loc)
            print("now", player.coord)
            walls = tiles[0]
            doors = tiles[1]
            items = tiles[3]
            enemies = tiles[4]
            hides = tiles[5]
            spells = []
            
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
        screen.blit(settingsOpen.image, settingsOpen.rect)
        screen.blit(health.image, health.rect)
        screen.blit(speedPotions.image, speedPotions.rect)
        screen.blit(fullPotions.image, fullPotions.rect)
        screen.blit(halfPotions.image, halfPotions.rect)
        screen.blit(revivePotions.image, revivePotions.rect)
        screen.blit(healthPotions.image, healthPotions.rect)
        if popup != []:
            screen.blit(popup[0].image, popup[0].rect)
        if close != []:
            screen.blit(close[0].image, close[0].rect)
        screen.blit(position.image, position.rect)

    pygame.display.flip()
    clock.tick(60)
