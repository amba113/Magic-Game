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
from Stack import *

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

counter = 0

hp = Text2("HP: ", [150, 25])
speedPotions = Text("Speed Potions: ", [900-170, 2], 24)
fullPotions = Text("Full Heal Potions: ", [900-170, 17], 24)
halfPotions = Text("Half Heal Potions: ", [900-170, 32], 24)
revivePotions = Text("Revive Potions: ", [900-170, 700-20], 24)
healthPotions = Text("Health Potions: ", [900-170, 700-35], 24)
position = Text("X,Y: ", [5, 700-20], 24)

money = Text2("Coins: ", [3*900/4, 125], 36, "Yellow")
deathNote1 = Text2("You have no revive potions...you dead XD", [900/2, 700/2 - 50], 36)
deathNote2 = Text2("Pres s V to revive", [900/2, 700/2 - 50], 36)
deathNote3 = Text2("Press R to roam as a ghost", [900/2, 700/2 + 50], 36)
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
choice = ""
popup = []
buttons = []
options = []
pet = ""
petEquip = ""

closeButton = SettingsButton([770, 125], "close")
backButton = SettingsButton([135, 565], "back")

loc = ""
views = Stack("game")
viewChanged = False

controls = {"forward": "w",
            "backward": "s",
            "left": "a",
            "right": "d",
            "speed": "g",
            "half": "h",
            "full": "f",
            "health": "t",
            "inventory": "e"}
            
while True:
    if views.top() == "game":
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
                elif event.key == pygame.K_r and player.dead:
                    player.roam = True
                    
                elif event.key == pygame.key.key_code(controls["left"]) or event.key == pygame.K_LEFT:
                    player.goKey("left")
                elif event.key == pygame.key.key_code(controls["right"]) or event.key == pygame.K_RIGHT:
                    player.goKey("right")
                elif event.key == pygame.key.key_code(controls["forward"]) or event.key == pygame.K_UP:
                    player.goKey("up")
                elif event.key == pygame.key.key_code(controls["backward"]) or event.key == pygame.K_DOWN:
                    player.goKey("down")
                
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    player.sprinting = True
                    
                elif event.key == pygame.key.key_code(controls["full"]):
                    player.useItem("f")
                elif event.key == pygame.key.key_code(controls["half"]):
                    player.useItem("h")
                elif event.key == pygame.key.key_code(controls["speed"]):
                    player.useItem("g")
                elif event.key == pygame.K_v:
                    if player.dead:
                        player.goto(tiles[2])
                    player.useItem("v")
                    for enemy in enemies:
                        enemy.angry = False
                elif event.key == pygame.key.key_code(controls["health"]):
                    player.useItem("t")
                    
                elif event.key == pygame.key.key_code(controls["inventory"]):
                    views.push("inventory")
                    viewChanged = True

                elif event.key == pygame.K_1:
                    spellType = "basic"
                elif event.key == pygame.K_2:
                    if "basic2" in player.spells:
                        spellType = "basic2"
                        
                elif event.key == pygame.K_c:
                    if "calicoCat" in player.inventory["pets"]:
                        petEquip = "calicoCat"
                        pet = Pet([player.rect.center[0] - 1, player.rect.center[1] - 1], petEquip)
                elif event.key == pygame.K_b:
                    if "blackCat" in player.inventory["pets"]:
                        petEquip = "blackCat"
                        pet = Pet([player.rect.center[0] - 1, player.rect.center[1] - 1], petEquip)
                elif event.key == pygame.K_o:
                    if "owl" in player.inventory["pets"]:
                        petEquip = "owl"
                        pet = Pet([player.rect.center[0] - 1, player.rect.center[1] - 1], petEquip)
                elif event.key == pygame.K_k:
                    if "frog" in player.inventory["pets"]:
                        petEquip = "frog"
                        pet = Pet([player.rect.center[0] - 1, player.rect.center[1] - 1], petEquip)
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.key.key_code(controls["left"]) or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.key.key_code(controls["right"]) or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                elif event.key == pygame.key.key_code(controls["forward"]) or event.key == pygame.K_UP:
                    player.goKey("sup")
                elif event.key == pygame.key.key_code(controls["backward"]) or event.key == pygame.K_DOWN:
                    player.goKey("sdown")
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
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
                                    if event.key == pygame.pygame.key.key_code(controls["left"]) or event.key == pygame.K_LEFT:
                                        player.goKey("sleft")
                                    elif event.key == pygame.key.key_code(controls["right"]) or event.key == pygame.K_RIGHT:
                                        player.goKey("sright")
                                    elif event.key == pygame.key.key_code(controls["forward"]) or event.key == pygame.K_UP:
                                        player.goKey("sup")
                                    elif event.key == pygame.key.key_code(controls["backward"]) or event.key == pygame.K_DOWN:
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
                                            
                            if selected == "quit":
                                direct = "Rooms/Sav/"
                                files = os.listdir(direct)
                                for f in files:
                                    if f[-4:] == ".sav":
                                        os.remove("Rooms/Sav/" + f)
                                sys.exit()
                            elif selected == "store":
                                views.push("store")
                                viewChanged = True
                            elif selected == "controls":
                                views.push("controls")
                                viewChanged = True
                                
                            for button in buttons:
                                screen.blit(button.image, button.rect)
                            pygame.display.flip()
                            clock.tick(60)
                            
                    elif player.inventory["wand"] != None:
                        spells += [player.shoot(spellType, event.pos)]

        for wall in walls:
            player.wallTileCollide(wall)
        
        for item in items:
            if player.itemCollide(item):
                if item.kind == "wand":
                    views.push("wandChoice")
                    viewChanged = True
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
        
        if petEquip != "":        
            for enemy in enemies:
                if enemy.angry == True:
                    pet.update(player.rect.center, True, enemy.rect.center)
                else:
                    pet.update(player.rect.center)
                enemy.petCollide(pet)
            pet.update(player.rect.center)

        for spell in spells:
            spell.update()
        
        hp.update(str(player.hp) + "/" + str(player.hpMax))
        position.update(str(player.coord[0]) + "," + str(player.coord[1]))
        
        speedPotions.update(player.inventory["speedPotion"])
        fullPotions.update(player.inventory["fullHealPotion"])
        halfPotions.update(player.inventory["halfHealPotion"])
        revivePotions.update(player.inventory["revivePotion"])
        healthPotions.update(player.inventory["healthPotion"])
        money.update(player.inventory["coins"])
        
        deathNote1.update("")
        deathNote2.update("")
        deathNote3.update("")
        
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
                spells = []
                
                player.goto(tiles[2])
                if petEquip != "":
                    pet.goto(tiles[2])

        screen.fill((250, 175, 225))    
                
        for spell in spells:
            if not spell.living:
                spells.remove(spell)
                
        for enemy in enemies:
            if not enemy.living:
                enemies.remove(enemy)


        if player.dead and not player.roam:
            if player.inventory["revivePotion"] > 0:
                screen.blit(deathNote2.image, deathNote2.rect)
                screen.blit(deathNote3.image, deathNote3.rect)
            elif player.inventory["revivePotion"] == 0:
                screen.blit(deathNote1.image, deathNote1.rect)
                screen.blit(deathNote3.image, deathNote3.rect)
        elif player.dead and player.roam:
            for wall in walls:
                screen.blit(wall.image, wall.rect)
            screen.blit(pet.image, pet.rect)
            for door in doors:
                screen.blit(door.image, door.rect)
            screen.blit(player.image, player.rect)
            for hide in hides:
                screen.blit(hide.image, hide.rect)
        else:
            for wall in walls:
                screen.blit(wall.image, wall.rect)
            for item in items:
                screen.blit(item.image, item.rect)
            for spell in spells:
                screen.blit(spell.image, spell.rect)
            for enemy in enemies:
                screen.blit(enemy.image, enemy.rect)
            if petEquip != "":
                screen.blit(pet.image, pet.rect)
            for door in doors:
                screen.blit(door.image, door.rect)
            screen.blit(player.image, player.rect)
            for hide in hides:
                screen.blit(hide.image, hide.rect)
            screen.blit(settingsOpen.image, settingsOpen.rect)
            screen.blit(hp.image, hp.rect)
            screen.blit(speedPotions.image, speedPotions.rect)
            screen.blit(fullPotions.image, fullPotions.rect)
            screen.blit(halfPotions.image, halfPotions.rect)
            screen.blit(revivePotions.image, revivePotions.rect)
            screen.blit(healthPotions.image, healthPotions.rect)
            screen.blit(position.image, position.rect)
            
        pygame.display.flip()
        clock.tick(60)
        
    if views.top() == "wandChoice":
        while viewChanged:
            choice = ""
            popup = [Popup("wandChoice", [size[0]/2, size[1]/2])]
            buttons = [WandButton("basic", [(size[0]/2)/2 + 40, (size[1]/2)]),
                       WandButton("colorful", [(size[0]/2) - 60, (size[1]/2)]),
                       WandButton("swirl", [(size[0]/2) + 60, (size[1]/2)]),
                       WandButton("candyCane", [3*(size[0]/2)/2 - 40, (size[1]/2)])]
            viewChanged = False
        while choice == "":
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
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        if button.click(event.pos):
                            choice = button.kind            

            screen.blit(popup[0].image, popup[0].rect)
            for button in buttons:
                screen.blit(button.image, button.rect)
            pygame.display.flip()
        
        views = Stack("game")
        player.kind = choice + "Wand"                     

    if views.top() == "controls":
        if viewChanged:
            goodInput = True
            offsety = 125
            offsetx = 50
            color = [0, 255, 245]
            color2 = [230, 230, 230]
            popup = [Popup("controls", [size[0]/2, size[1]/2])]
            reset = SettingsButton([900/2, 500 + offsety], "reset")
            error = Text2("Error, this control key is already in use", [900/2, 55 + offsety], 48, "Red")   
            options = [SettingsButton([600/3 + offsetx, 400/3 + offsety], "controlsBox"),
                       SettingsButton([2*600/3 + offsetx, 400/3 + offsety], "controlsBox"),
                       SettingsButton([600 + offsetx, 400/3 + offsety], "controlsBox"),
                       SettingsButton([600/3 + offsetx, 2*400/3 + offsety], "controlsBox"),
                       SettingsButton([2*600/3 + offsetx, 2*400/3 + offsety], "controlsBox"),
                       SettingsButton([600 + offsetx, 2*400/3 + offsety], "controlsBox"),
                       SettingsButton([600/3 + offsetx, 400 + offsety], "controlsBox"),
                       SettingsButton([2*600/3 + offsetx, 400 + offsety], "controlsBox"),
                       SettingsButton([600 + offsetx, 400 + offsety], "controlsBox")]
            staticTexts = [Text2("Forward", [600/3 + offsetx, 400/3 - 35 + offsety], 36, color),
                           Text2("Backward", [2*600/3 + offsetx, 400/3 - 35 + offsety], 36, color),
                           Text2("Left", [600 + offsetx, 400/3 - 35 + offsety], 36, color),
                           Text2("Right", [600/3 + offsetx, 2*400/3 - 35 + offsety], 36, color),
                           Text2("Speed Potion", [2*600/3 + offsetx, 2*400/3 - 35 + offsety], 36, color),
                           Text2("Half Heal Potion", [600 + offsetx, 2*400/3 - 35 + offsety], 36, color),
                           Text2("Full Heal Potion", [600/3 + offsetx, 400 - 35 + offsety], 36, color),
                           Text2("Health Potion", [2*600/3 + offsetx, 400 - 35 + offsety], 36, color),
                           Text2("Inventory", [600 + offsetx, 400 - 35 + offsety], 36, color)]
            dynamicTexts = [Text2(controls["forward"].upper(), [600/3 + offsetx, 400/3 + 2 + offsety], 36, color2),
                            Text2(controls["backward"].upper(), [2*600/3 + offsetx, 400/3 + 2 + offsety], 36, color2),
                            Text2(controls["left"].upper(), [600 + offsetx, 400/3 + 2 + offsety], 36, color2),
                            Text2(controls["right"].upper(), [600/3 + offsetx, 2*400/3 + 2 + offsety], 36, color2),
                            Text2(controls["speed"].upper(), [2*600/3 + offsetx, 2*400/3 + 2 + offsety], 36, color2),
                            Text2(controls["half"].upper(), [600 + offsetx, 2*400/3 + 2 + offsety], 36, color2),
                            Text2(controls["full"].upper(), [600/3 + offsetx, 400 + 2 + offsety], 36, color2),
                            Text2(controls["health"].upper(), [2*600/3 + offsetx, 400 + 2 + offsety], 36, color2),
                            Text2(controls["inventory"].upper(), [600 + offsetx, 400 + 2 + offsety], 36, color2)]
            key = ""
            tempKey = False
            index = 0
            viewChanged = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if goodInput:
                        if closeButton.click(event.pos):
                            selected = ""
                            views = Stack("game")
                    if reset.click(event.pos):
                        controls["forward"] = "w"
                        controls["backward"] = "s"
                        controls["left"] = "a"
                        controls["right"] = "d"
                        controls["speed"] = "g"
                        controls["half"] = "h"
                        controls["full"] = "f"
                        controls["health"] = "t"
                        controls["inventory"] = "e"
                        
                        dynamicTexts[0].baseText = controls["forward"].upper()
                        dynamicTexts[1].baseText = controls["backward"].upper()
                        dynamicTexts[2].baseText = controls["left"].upper()
                        dynamicTexts[3].baseText = controls["right"].upper()
                        dynamicTexts[4].baseText = controls["speed"].upper()
                        dynamicTexts[5].baseText = controls["half"].upper()
                        dynamicTexts[6].baseText = controls["full"].upper()
                        dynamicTexts[7].baseText = controls["health"].upper()
                        dynamicTexts[8].baseText = controls["inventory"].upper()
                        
                    for i, option in enumerate(options):
                        if option.click(event.pos):
                            index = i
                            tempKey = True
            
            if tempKey == True and event.type == pygame.KEYDOWN:
                opt = event.unicode
                if staticTexts[index].baseText.lower() == "forward":
                    controls["forward"] = opt
                elif staticTexts[index].baseText.lower() == "backward":
                    controls["backward"] = opt
                elif staticTexts[index].baseText.lower() == "left":
                    controls["left"] = opt
                elif staticTexts[index].baseText.lower() == "right":
                    controls["right"] = opt
                elif staticTexts[index].baseText.lower() == "speed potion":
                    controls["speed"] = opt
                elif staticTexts[index].baseText.lower() == "full heal potion":
                    controls["full"] = opt
                elif staticTexts[index].baseText.lower() == "half heal potion":
                    controls["half"] = opt
                elif staticTexts[index].baseText.lower() == "health potion":
                    controls["health"] = opt
                elif staticTexts[index].baseText.lower() == "inventory":
                    controls["inventory"] = opt
                
                dynamicTexts[index].baseText = event.unicode.upper()
                tempKey = False
       
        goodInput = True
        for i in controls.keys():
            for x in controls.keys():
                if i != x and controls[i] == controls[x]:
                    goodInput = False
            
        for text in staticTexts:
            text.update("")
        for text in dynamicTexts:
            text.update("")
        error.update("")
        
        screen.blit(popup[0].image, popup[0].rect)
        if goodInput == True:
            screen.blit(closeButton.image, closeButton.rect)
        else:
            screen.blit(error.image, error.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        for text in staticTexts:
            screen.blit(text.image, text.rect)
        for text in dynamicTexts:
            screen.blit(text.image, text.rect)
        screen.blit(reset.image, reset.rect)
        pygame.display.flip()
        
    if views.top() == "store":
        if viewChanged:
            popup = [Popup("store", [size[0]/2, size[1]/2])]
            options = [SettingsButton([900/2, 225], "petsSt"),
                        SettingsButton([900/2, 325], "spellsSt"),
                        SettingsButton([900/2, 425], "potionsSt"),
                        SettingsButton([900/2, 525], "clothesSt")]
            viewChanged = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    for option in options:
                        if option.click(event.pos):
                            options = []
                            views.push(option.kind)
                            viewChanged = True
                            
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()

    if views.top() == "petsSt":
        if viewChanged:
            options = [StoreChoice([900/3, 275], views.top(), "blackCat"),
                       StoreChoice([2*900/3, 275], views.top(), "calicoCat"),
                       StoreChoice([900/3, 450], views.top(), "owl"),
                       StoreChoice([2*900/3, 450], views.top(), "frog")]
            viewChanged = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    for option in options:
                        if option.click(event.pos):
                            player.purchase(option.kind, "pet")
        
        money.update(player.inventory["coins"])
        
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()

    if views.top() == "spellsSt":
        if viewChanged:
            options = [StoreChoice([900/2, 700/2], views.top(), "simple")]
            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    for option in options:
                        if option.click(event.pos):
                            player.purchase(option.kind, "spell")
        
        money.update(player.inventory["coins"])
        
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
        
    if views.top() == "potionsSt":
        if viewChanged:
            options = [StoreChoice([900/3, 275], views.top(), "fullHeal"),
                       StoreChoice([2*900/3, 275], views.top(), "halfHeal"),
                       StoreChoice([900/4, 450], views.top(), "health"),
                       StoreChoice([900/2, 450], views.top(), "revive"),
                       StoreChoice([3*900/4, 450], views.top(), "speed")]
            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    for option in options:
                        if option.click(event.pos):
                            player.purchase(option.kind, "potion")
                 
        money.update(player.inventory["coins"])
                                
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
                                
    if views.top() == "clothesSt":
        if viewChanged:
            options = [StoreChoice([900/2, 700/2], views.top(), "simple")]
            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    for option in options:
                        if option.click(event.pos):
                            player.purchase(option.kind, "clothing")
        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
        
    if views.top() == "inventory":
        if viewChanged:
            popup = [Popup("inventory", [900/2, 700/2])]
            options = [SettingsButton([900/2, 225], "petsIn"),
                        SettingsButton([900/2, 325], "spellsIn"),
                        SettingsButton([900/2, 425], "potionsIn"),
                        SettingsButton([900/2, 525], "clothesIn")]
            viewChanged = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    for option in options:
                        if option.click(event.pos):
                            options = []
                            views.push(option.kind)
                            viewChanged = True

        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        pygame.display.flip()

    if views.top() == "petsIn":
            if viewChanged:
                options = [StoreChoice([900/2, 700/2], "spellsSt", "simple")]
                viewChanged = False
                           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    direct = "Rooms/Sav/"
                    files = os.listdir(direct)
                    for f in files:
                        if f[-4:] == ".sav":
                            os.remove("Rooms/Sav/" + f)
                    sys.exit();
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if closeButton.click(event.pos):
                            selected = ""
                            views = Stack("game")
                        if backButton.click(event.pos):
                            views.pop()
                            viewChanged = True
                        for option in options:
                            if option.click(event.pos):
                                pass
                                #Equip or delete, depending on category
                                    
            screen.blit(popup[0].image, popup[0].rect)
            screen.blit(closeButton.image, closeButton.rect)
            screen.blit(backButton.image, backButton.rect)
            for option in options:
                screen.blit(option.image, option.rect)
            pygame.display.flip()

    if views.top() == "spellsIn":
            if viewChanged:
                options = [StoreChoice([900/2, 700/2], "spellsSt", "simple")]
                viewChanged = False
                           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    direct = "Rooms/Sav/"
                    files = os.listdir(direct)
                    for f in files:
                        if f[-4:] == ".sav":
                            os.remove("Rooms/Sav/" + f)
                    sys.exit();
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if closeButton.click(event.pos):
                            selected = ""
                            views = Stack("game")
                        if backButton.click(event.pos):
                            views.pop()
                            viewChanged = True
                        for option in options:
                            if option.click(event.pos):
                                pass
                                #Equip or delete, depending on category
                                    
            screen.blit(popup[0].image, popup[0].rect)
            screen.blit(closeButton.image, closeButton.rect)
            screen.blit(backButton.image, backButton.rect)
            for option in options:
                screen.blit(option.image, option.rect)
            pygame.display.flip()
            
    if views.top() == "potionsIn":
            if viewChanged:
                options = [StoreChoice([900/2, 700/2], "spellsSt", "simple")]
                viewChanged = False
                           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    direct = "Rooms/Sav/"
                    files = os.listdir(direct)
                    for f in files:
                        if f[-4:] == ".sav":
                            os.remove("Rooms/Sav/" + f)
                    sys.exit();
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if closeButton.click(event.pos):
                            selected = ""
                            views = Stack("game")
                        if backButton.click(event.pos):
                            views.pop()
                            viewChanged = True
                        for option in options:
                            if option.click(event.pos):
                                pass
                                #Equip or delete, depending on category
                                    
            screen.blit(popup[0].image, popup[0].rect)
            screen.blit(closeButton.image, closeButton.rect)
            screen.blit(backButton.image, backButton.rect)
            for option in options:
                screen.blit(option.image, option.rect)
            pygame.display.flip()
            
    if views.top() == "clothesIn":
        if viewChanged:
            options = [StoreChoice([900/2, 700/2], "spellsSt", "simple")]
            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                direct = "Rooms/Sav/"
                files = os.listdir(direct)
                for f in files:
                    if f[-4:] == ".sav":
                        os.remove("Rooms/Sav/" + f)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    for option in options:
                        if option.click(event.pos):
                            pass
                            #Equip or delete, depending on category
                                
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        pygame.display.flip()
