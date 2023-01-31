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
from StoreOptions import *
from Pets import *

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

money = Text2("Coins: ", [3*900/4, 125], 36, "Yellow")
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
options = []
pets = []

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
            if event.button== 1:
                if settingsOpen.click(event.pos):
                    selected = ""
                    setOpen = True
                    buttons = [SettingsButton([60, 65], "controls"),
                               SettingsButton([60, 115], "store"),
                               SettingsButton([60, 165], "quit")]
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
                                if event.button == 1:
                                    buttonClicked = False
                                    for button in buttons:
                                        if button.click(event.pos):
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
                    spells += [player.shoot(spellType, event.pos)]
                if selected == 2:
                    popup = [Popup("store", [size[0]/2, size[1]/2])]
                    close = [SettingsButton([770, 125], "close")]
                    options = [SettingsButton([900/2, 225], "pets"),
                                SettingsButton([900/2, 325], "spells"),
                                SettingsButton([900/2, 425], "potions"),
                                SettingsButton([900/2, 525], "clothes")]
                    if event.button == 1:
                        if close[0].click(event.pos):
                            selected = ""
                            popup = []
                            close = []
                        for option in options:
                            if option.click(event.pos):
                                if option.kind == "pets":
                                    options = []
                                    options = [StoreChoice([900/3, 225], option.kind, "blackCat"),
                                               StoreChoice([2*900/3, 225], option.kind, "calicoCat"),
                                               StoreChoice([900/3, 450], option.kind, "owl"),
                                               StoreChoice([2*900/3, 450], option.kind, "frog")]
                                    if event.button == 1:
                                        for option in options:
                                            if option.click(event.pos):
                                                if player.purchase(option.kind, "pet"):
                                                    pets += [Pet([player.rect.center[0] - 1, player.rect.center[1] - 1], option.kind)]
                                elif option.kind == "spells":
                                    print("Spells chosen")
                                elif option.kind == "potions":
                                    options = []
                                    options = [StoreChoice([900/3, 225], option.kind, "fullHeal"),
                                               StoreChoice([2*900/3, 225], option.kind, "halfHeal"),
                                               StoreChoice([900/4, 450], option.kind, "health"),
                                               StoreChoice([900/2, 450], option.kind, "revive"),
                                               StoreChoice([3*900/4, 450], option.kind, "speed")]
                                    if event.button == 1:
                                        for option in options:
                                            if option.click(event.pos):
                                                player.purchase(option.kind, "potion")
                                elif option.kind == "clothes":
                                    print("Clothes chosen")
                                else:
                                    print("Error")
                    else:
                        pass
                
    
    for wall in walls:
        player.wallTileCollide(wall)
    
    for item in items:
        if player.itemCollide(item):
            if item.kind == "wand":
                selected = ""
                popup = Popup("wandChoice", [size[0]/2, size[1]/2])
                buttons = [WandButton("basic", [(size[0]/2)/2 + 40, (size[1]/2)]),
                           WandButton("colorful", [(size[0]/2) - 60, (size[1]/2)]),
                           WandButton("swirl", [(size[0]/2) + 60, (size[1]/2)]),
                           WandButton("candyCane", [3*(size[0]/2)/2 - 40, (size[1]/2)])]
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
                        if event.type == 1:
                            for button in buttons:
                                if button.click(event.pos):
                                    selected = button.kind
                    print(selected)
                    

                    screen.blit(popup.image, popup.rect)
                    for button in buttons:
                        screen.blit(button.image, button.rect)
                    pygame.display.flip()
                    clock.tick(60)
                player.kind = selected                        
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
    
    for pet in pets:
        for enemy in enemies:
            if enemy.angry == True:
                print("pet defend")
                pet.update(player.rect.center, True, enemy.rect.center)
            else:
                print("pet follow")
                pet.update(player.rect.center)
            enemy.petCollide(pet)

    for spell in spells:
        spell.update()
    
    health.update(str(player.hp) + "/" + str(player.hpMax))
    position.update(str(player.coord[0]) + "," + str(player.coord[1]))
    
    speedPotions.update(player.inventory["speedPotion"])
    fullPotions.update(player.inventory["fullHealPotion"])
    halfPotions.update(player.inventory["halfHealPotion"])
    revivePotions.update(player.inventory["revivePotion"])
    healthPotions.update(player.inventory["healthPotion"])
    money.update(player.inventory["coins"])
    
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
            
            player.goto(tiles[2])

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
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        if selected == 2:
            screen.blit(popup[0].image, popup[0].rect)
            screen.blit(close[0].image, close[0].rect)
            for option in options:
                screen.blit(option.image, option.rect)
            screen.blit(money.image, money.rect)
        else:
            for item in items:
                screen.blit(item.image, item.rect)
            for spell in spells:
                screen.blit(spell.image, spell.rect)
            for enemy in enemies:
                screen.blit(enemy.image, enemy.rect)
            for pet in pets:
                screen.blit(pet.image, pet.rect)
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
        screen.blit(position.image, position.rect)
        
    pygame.display.flip()
    clock.tick(60)
