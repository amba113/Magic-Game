import pygame, sys, math, random, os, pickle, shutil
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
from InventoryOptions import *
from Pets import *
from Stack import *
from HealthBar import *
from Sprite import *
from Prices import *

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

counter = 0

position = Text("X,Y: ", [5, 700-20], 24)

money = Text2("Coins: ", [3*900/4, 125], 36, "Yellow")
deathNote1 = Text2("You have no revive potions...you dead XD", [900/2, 700/2 - 50], 36)
deathNote2 = Text2("Press ", [900/2, 700/2 - 50], 36)
deathNote3 = Text2("Press R to roam as a ghost\nPress S to start over", [900/2, 700/2 + 50], 36)
deathNote4 = Text2("You have enough coins to get revive\nPress ", [900/2, 700/2 - 50], 36)
settingsOpen = SettingsOpen([25, 25])

tiles = loadMap("test")
walls = tiles[0]
doors = tiles[1]
hides = tiles[5]
player = Player(4, tiles[2])
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

hp = Health(player.coord, [10, 60], 3)

closeButton = SettingsButton([770, 125], "close")
backButton = SettingsButton([135, 565], "back")
playButton = SettingsButton([900/2, 500], "play")
signButton = SettingsButton([900/2, 500], "sign")
passSee = SettingsButton([900/2 + 125, 375], "passSee")
passHide = SettingsButton([900/2 + 125, 375], "passHide")

titleText = Text2("[Insert Game Name]", [900/2, 200], 100)

loc = ""
views = Stack("title")
viewChanged = True

controls = {"forward": "w",
            "backward": "s",
            "left": "a",
            "right": "d",
            "speed": "g",
            "half": "h",
            "full": "f",
            "health": "t",
            "revive": "v",
            "inventory": "e",
            "store": "b"}
            
color1 = (255, 255, 255)
color2 = (0, 0, 0)
box1 = False
box2 = False
box3 = False
name = False
add = False
agree = False
baseFont = pygame.font.Font(None, 40)
userText1 = ''
userText2 = ''
userText3 = ''
user = ''
stars = ''
see = False
inputRect1 = pygame.Rect(size[0]/2 - 200/2, size[1]/4, 200, 50)
inputRect2 = pygame.Rect(size[0]/2 - 200/2, size[1]/2, 200, 50)
inputRect3 = pygame.Rect(size[0]/2 - 200/2, 3*size[1]/8, 200, 50)
agreeRect = pygame.Rect(size[0]/2 - 150/2, size[1]/3, 150, 50)
disagreeRect = pygame.Rect(size[0]/2 - 150/2, 2*size[1]/3, 150, 50)
r1 = False
r2 = False
r3 = False
rA = False
rD = False
rP = False  

test = False
escape = False

def doSignin(name, pwd):
    direct = "Data/logins.txt"
    f = open(direct, 'r')
    lines = f.readlines()
    f.close()
    user = None
    username = None
    newLines = []
    good = False
    new = False
    
    for l in lines:
        newLine = l.split(" ")
        newLines += [newLine]
    z = 0
    for i, line in enumerate(newLines):
        if name == line[0]:
            if pwd == line[1]:
                z = i
                good = True
            else:
                good = False
                print("no match")
            new = False
        else:
            new = True
            
        if good == True:
            temp = newLines[z]
            user = temp[0]
            username = temp[2]

    f.close()
    return user, username, new
            
while True:
    if views.top() == "title":
        if viewChanged:
            box1 = False
            box2 = False
            box3 = False
            name = False
            add = False
            agree = False
            userText1 = ''
            userText2 = ''
            userText3 = ''
            user = ''
            stars = ''
            see = False
            viewChanged = False
            if os.path.isdir("Data/Test"):
                shutil.rmtree("Data/Test")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit();
                elif event.key == pygame.K_t:
                    test = True
                    path = "Data/Test"
                    isdir = os.path.isdir(path)

                    if isdir:
                        print("exists")
                    else:
                        os.mkdir(path)
                        isdir = os.path.isdir(path)
                        print("made")
                        
                    path2 = "Data/Test/Rooms"
                    isdir = os.path.isdir(path2)

                    if isdir:
                        print("exists")
                    else:
                        os.mkdir(path2)
                        isdir = os.path.isdir(path2)
                        print("made")
                        
                    path3 = "Data/Test/Inventory"
                    isdir = os.path.isdir(path3)

                    if isdir:
                        pass
                    else:
                        os.mkdir(path3)
                        isdir = os.path.isdir(path3)
                    user = "Test"
                    tiles = loadMap(user)
                    walls = tiles[0]
                    doors = tiles[1]
                    hides = tiles[5]
                    player = Player(4, tiles[2])
                    items = tiles[3]
                    enemies = tiles[4]
                    spells = []
                    if tiles[6] != None:
                        player.inventory = tiles[6]
                    if tiles[9] != None:
                        controls = tiles[8]
                    if tiles[8] != None:
                        player.colorChoice, player.eyeChoice, player.mouthChoice, player.glassesChoice, player.hatChoice, player.shirtChoice = tiles[8]
                    player.hp = tiles[7]
                    views = Stack("game")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if signButton.click(event.pos):
                        views.push("signin")
        
        titleText.update("")
        
        screen.fill((250, 175, 225))
        screen.blit(titleText.image, titleText.rect)
        screen.blit(signButton.image, signButton.rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    if views.top() == "signin":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if inputRect1.collidepoint(event.pos) and r1:
                        box1 = True
                        box2 = False
                        box3 = False
                    elif inputRect2.collidepoint(event.pos) and r2:
                        box1 = False
                        box2 = True
                        box3 = False
                    elif inputRect3.collidepoint(event.pos) and r3:
                        box1 = False
                        box2 = False
                        box3 = True
                    elif agreeRect.collidepoint(event.pos) and rA:
                        agree = True
                    elif disagreeRect.collidepoint(event.pos) and rD:
                        views.pop()
                        viewChanged = True
                    elif playButton.click(event.pos) and rP:
                        user, username, new = doSignin(userText1, userText2)
                        print(user, username)
                        if name:
                            print("NEW")
                            if userText3 != "":
                                add = userText1 + " " + userText2 + " " + userText3 + "\n"
                                
                                direct = "logins.txt"
                                a = open(direct, 'a')
                                a.write(add)
                                a.close()
                                name = False
                                path = "Rooms/Sav/" + userText1
                                isdir = os.path.isdir(path)

                                if isdir:
                                    print("exists")
                                else:
                                    os.mkdir(path)
                                    isdir = os.path.isdir(path)
                                    print("made")
                                path2 = "Inventories/" + userText1
                                isdir = os.path.isdir(path2)

                                if isdir:
                                    pass
                                else:
                                    os.mkdir(path2)
                                    isdir = os.path.isdir(path2)
                                user = userText1
                                tiles = loadMap(user)
                                walls = tiles[0]
                                doors = tiles[1]
                                hides = tiles[5]
                                player = Player(4, tiles[2])
                                items = tiles[3]
                                enemies = tiles[4]
                                spells = []
                                if tiles[6] != None:
                                    player.inventory = tiles[6]
                                if tiles[9] != None:
                                    controls = tiles[8]
                                if tiles[8] != None:
                                    player.colorChoice, player.eyeChoice, player.mouthChoice, player.glassesChoice, player.hatChoice, player.shirtChoice = tiles[8]
                                player.hp = tiles[7]
                                views = Stack("game")
                            else:
                                print("no input", userText3)
                            
                        elif user == None or username == None:
                            if new:
                                print("new")
                                add = new
                            else:
                                print("Clear")
                                box1 = False
                                box2 = False
                                box3 = False
                                userText1 = ""
                                userText2 = ""
                                userText3 = ""
                                stars = ''
                        else:
                            path = "Rooms/Sav/" + userText1
                            isdir = os.path.isdir(path)

                            if isdir:
                                print("exists")
                            else:
                                os.mkdir(path)
                                isdir = os.path.isdir(path)
                                print("made")
                            path2 = "Inventories/" + userText1
                            isdir = os.path.isdir(path2)

                            if isdir:
                                pass
                            else:
                                os.mkdir(path2)
                                isdir = os.path.isdir(path2)
                            user = userText1
                            tiles = loadMap(user)
                            walls = tiles[0]
                            doors = tiles[1]
                            hides = tiles[5]
                            player = Player(4, tiles[2])
                            items = tiles[3]
                            enemies = tiles[4]
                            spells = []
                            if tiles[6] != None:
                                player.inventory = tiles[6]
                            if tiles[9] != None:
                                controls = tiles[8]
                            if tiles[8] != None:
                                player.colorChoice, player.eyeChoice, player.mouthChoice, player.glassesChoice, player.hatChoice, player.shirtChoice = tiles[8]
                            player.hp = tiles[7]
                            views = Stack("game")
                    
                    elif see and passSee.click(event.pos):
                        see = False        
                    elif not see and passHide.click(event.pos):
                        see = True        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if box1:
                        userText1 = userText1[:-1]
                    elif box2:
                        userText2 = userText2[:-1]
                        stars = stars[:-1]
                    elif box3:
                        userText3 = userText3[:-1]
                elif event.key == pygame.K_RETURN:
                    user, username, new = doSignin(userText1, userText2)
                    print(user, username)
                    if name:
                        if userText3 != "":
                            add = userText1 + " " + userText2 + " " + userText3 + "\n"
                            
                            direct = "logins.txt"
                            a = open(direct, 'a')
                            a.write(add)
                            a.close()
                            name = False
                            path = "Rooms/Sav/" + userText1
                            isdir = os.path.isdir(path)

                            if isdir:
                                print("exists")
                            else:
                                os.mkdir(path)
                                isdir = os.path.isdir(path)
                                print("made")
                            path2 = "Inventories/" + userText1
                            isdir = os.path.isdir(path2)

                            if isdir:
                                pass
                            else:
                                os.mkdir(path2)
                                isdir = os.path.isdir(path2)
                            user = userText1
                            tiles = loadMap(user)
                            walls = tiles[0]
                            doors = tiles[1]
                            hides = tiles[5]
                            player = Player(4, tiles[2])
                            items = tiles[3]
                            enemies = tiles[4]
                            spells = []
                            if tiles[6] != None:
                                player.inventory = tiles[6]
                            if tiles[9] != None:
                                controls = tiles[8]
                            if tiles[8] != None:
                                player.colorChoice, player.eyeChoice, player.mouthChoice, player.glassesChoice, player.hatChoice, player.shirtChoice = tiles[8]
                            player.hp = tiles[7]
                            views = Stack("game")
                        else:
                            print("no input", userText3)
                        
                    elif user == None or username == None:
                        if new:
                            add = new
                        else:
                            box1 = False
                            box2 = False
                            box3 = False
                            userText1 = ""
                            userText2 = ""
                            userText3 = ""
                            stars = ''
                    else:
                        path = "Rooms/Sav/" + userText1
                        isdir = os.path.isdir(path)

                        if isdir:
                            print("exists")
                        else:
                            os.mkdir(path)
                            isdir = os.path.isdir(path)
                            print("made")
                        path2 = "Inventories/" + userText1
                        isdir = os.path.isdir(path2)

                        if isdir:
                            pass
                        else:
                            os.mkdir(path2)
                            isdir = os.path.isdir(path2)
                        user = userText1
                        tiles = loadMap(user)
                        walls = tiles[0]
                        doors = tiles[1]
                        hides = tiles[5]
                        player = Player(4, tiles[2])
                        items = tiles[3]
                        enemies = tiles[4]
                        spells = []
                        if tiles[6] != None:
                            player.inventory = tiles[6]
                        if tiles[9] != None:
                            controls = tiles[8]
                        if tiles[8] != None:
                            [player.colorChoice, player.eyeChoice, player.mouthChoice, player.glassesChoice, player.hatChoice, player.shirtChoice] = tiles[8]
                        player.hp = tiles[7]
                        views = Stack("game")
                                                    
                elif event.key == pygame.K_TAB:
                    if box1:
                        box1 = False
                        box2 = True
                    elif box2:
                        box1 = True
                        box2 = False

                else:
                    if box1:
                        userText1 += event.unicode
                    elif box2:
                        userText2 += event.unicode
                        stars += "*"
                    elif box3:
                        userText3 += event.unicode
        
        
        screen.fill(color1)
        
        if add and agree:
            r1 = False
            r2 = False
            r3 = True
            rA = False
            rD = False
            rP = True
            screen.blit(playButton.image, playButton.rect)
            
            label3 = baseFont.render("Screen Name:", True, color2)
            textSurface3 = baseFont.render(userText3, True, color1)
            pygame.draw.rect(screen, color2, inputRect3)
            screen.blit(textSurface3, (inputRect3.x+5, inputRect3.y+5))
            screen.blit(label3, (inputRect3.x, inputRect3.y - 30))
            name = True
            
        elif add and not agree:
            r1 = False
            r2 = False
            r3 = False
            rA = True
            rD = True
            rP = False
            
            yes = baseFont.render("Yes", True, color1)
            no = baseFont.render("No", True, color1)
            warn = baseFont.render("This account does not exist, make a new one?", True, color2)
            pygame.draw.rect(screen, color2, agreeRect)
            pygame.draw.rect(screen, color2, disagreeRect)
            screen.blit(yes, (agreeRect.x+5, agreeRect.y+5))
            screen.blit(no, (disagreeRect.x+5, disagreeRect.y+5))
            screen.blit(warn, (100, 100))
        elif not add and not agree:
            r1 = True
            r2 = True
            r3 = False
            rA = False
            rD = False
            rP = True            
            
            label1 = baseFont.render("Username:", True, color2)
            textSurface1 = baseFont.render(userText1, True, color1)
            pygame.draw.rect(screen, color2, inputRect1)
            screen.blit(textSurface1, (inputRect1.x+5, inputRect1.y+5))
            screen.blit(label1, (inputRect1.x, inputRect1.y - 30))
            
            label2 = baseFont.render("Password:", True, color2)
            if see:
                screen.blit(passSee.image, passSee.rect)
                textSurface2 = baseFont.render(userText2, True, color1)
            elif not see:
                screen.blit(passHide.image, passHide.rect)
                textSurface2 = baseFont.render(stars, True, color1)
            pygame.draw.rect(screen, color2, inputRect2)
            screen.blit(textSurface2, (inputRect2.x+5, inputRect2.y+5))
            screen.blit(label2, (inputRect2.x, inputRect2.y - 30))
            
            screen.blit(playButton.image, playButton.rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    if views.top() == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player)
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                elif event.key == pygame.K_r and player.dead:
                    player.roam = True
                elif event.key == pygame.K_s and player.dead:
                    directs = ["/Rooms", "/Inventory"]
                    for d in directs:
                        direct = "Data/" + user + d
                        files = os.listdir(direct)
                        for f in files:
                            if f[-4:] == user:
                                nDirect = direct + f + "/"
                                check = os.listdir(nDirect)
                                for c in check:
                                    os.remove(nDirect + c)
                                os.rmdir(direct + f)
                    path = "Data/" + user + "/Rooms"
                    isdir = os.path.isdir(path)

                    if isdir:
                        print("exists")
                    else:
                        os.mkdir(path)
                        isdir = os.path.isdir(path)
                        print("made")
                    path2 = "Data/" + user + "/Inventory"
                    isdir = os.path.isdir(path2)

                    if isdir:
                        pass
                    else:
                        os.mkdir(path2)
                        isdir = os.path.isdir(path2)
                    tiles = loadMap(user)
                    walls = tiles[0]
                    doors = tiles[1]
                    hides = tiles[5]
                    player = Player(4, tiles[2])
                    items = tiles[3]
                    enemies = tiles[4]
                    spells = []
                    if tiles[6] != None:
                        player.inventory = tiles[6]
                    if tiles[9] != None:
                        controls = tiles[8]
                    if tiles[8] != None:
                        player.colorChoice, player.eyeChoice, player.mouthChoice, player.glassesChoice, player.hatChoice, player.shirtChoice = tiles[8]
                    player.hp = tiles[7]
                    
                elif event.key == pygame.K_c and test == True:
                    player.inventory["coins"] += 1
                    
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
                elif event.key == pygame.key.key_code(controls["revive"]):
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
                elif event.key == pygame.key.key_code(controls["store"]):
                    views.push("store")
                    viewChanged = True
                
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
                                   SettingsButton([60, 115], "signout"),
                                   SettingsButton([60, 165], "quit")]
                        popup = []
                        while selected == "" and setOpen == True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
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
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            elif selected == "signout":
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                views = Stack("title")
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
            enemy.wallCollide(size)
            for hide in hides:
                enemy.hideCollide(hide)
            for spell in spells:
                spell.collide(enemy)
                enemy.weaponCollide(spell)
            enemy.update(player.rect.center, size, player.hidden)
            if enemy.angry:
                player.hpHeal = False
            else:
                player.hpHeal = True
            if enemy.living == False and enemy.claimed == False:
                if enemy.kind == "basic":
                    player.inventory["coins"] += 3
                elif enemy.kind == "strong":
                    player.inventory["coins"] += 5
                else:
                    player.inventory["coins"] += 1
            if not enemy.living:
                enemies.remove(enemy)
            
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
        position.update(str(player.coord[0]) + "," + str(player.coord[1]))
        
        money.update(player.inventory["coins"])
        
        deathNote1.update("")
        deathNote2.update(controls["revive"].upper() + " to revive")
        deathNote3.update("")
        deathNote4.update(controls["revive"].upper() + " to spend " + " and revive")
        
        for door in doors:
            if player.doorCollide(door):
                for enemy in enemies:
                    enemy.angry = False
                player.hpHeal = True
                saveMap(user, items, enemies, player, controls, True)
                loc = door.kind
                tiles = loadMap(user, player.coord, loc)
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
            if petEquip != "":
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
            hp.update(player.rect.center, player.hp, player.hpMax, screen)
            for hide in hides:
                screen.blit(hide.image, hide.rect)
            screen.blit(settingsOpen.image, settingsOpen.rect)
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
                    if not test:
                        saveMap(user, items, enemies, player, controls)
                    sys.exit();
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        popup = Popup("escape", [size[0]/2, size[1]/2])
                        escape = True
                        while escape:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_y:
                                        escape = False
                                        if not test:
                                            saveMap(user, items, enemies, player, controls)
                                        sys.exit()
                                    elif event.key == pygame.K_n:
                                        escape = False
                            screen.blit(popup.image, popup.rect)
                            pygame.display.flip()
                            clock.tick(60)
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
        player.inventory["wand"] = choice                     

    if views.top() == "controls":
        if viewChanged:
            goodInput = True
            offsety = 125
            offsetx = 50
            statOffset = -40
            dynOffset = 2
            color = [20, 137, 255]
            color2 = [230, 230, 230]
            popup = [Popup("controls", [size[0]/2, size[1]/2])]
            reset = SettingsButton([900/2, 500 + offsety], "reset")
            error = Text2("Error, this control key is already in use", [900/2, 55 + offsety], 48, "Red")   
            options = [SettingsButton([600/4 + offsetx, 400/3 + offsety], "controlsBox"),
                       SettingsButton([2*600/4 + offsetx, 400/3 + offsety], "controlsBox"),
                       SettingsButton([3*600/4 + offsetx, 400/3 + offsety], "controlsBox"),
                       SettingsButton([600 + offsetx, 400/3 + offsety], "controlsBox"),
                       SettingsButton([600/4 + offsetx, 2*400/3 + offsety], "controlsBox"),
                       SettingsButton([2*600/4 + offsetx, 2*400/3 + offsety], "controlsBox"),
                       SettingsButton([3*600/4 + offsetx, 2*400/3 + offsety], "controlsBox"),
                       SettingsButton([600 + offsetx, 2*400/3 + offsety], "controlsBox"),
                       SettingsButton([600/3 + offsetx, 400 + offsety], "controlsBox"),
                       SettingsButton([2*600/3 + offsetx, 400 + offsety], "controlsBox"),
                       SettingsButton([600 + offsetx, 400 + offsety], "controlsBox")]
            staticTexts = [Text2("Forward", [600/4 + offsetx, 400/3 + statOffset + offsety], 36, color),
                           Text2("Backward", [2*600/4 + offsetx, 400/3 + statOffset + offsety], 36, color),
                           Text2("Left", [3*600/4 + offsetx, 400/3 + statOffset + offsety], 36, color),
                           Text2("Right", [600 + offsetx, 400/3 + statOffset + offsety], 36, color),
                           Text2("Speed", [600/4 + offsetx, 2*400/3 + statOffset + offsety], 36, color),
                           Text2("Half Heal", [2*600/4 + offsetx, 2*400/3 + statOffset + offsety], 36, color),
                           Text2("Full Heal", [3*600/4 + offsetx, 2*400/3 + statOffset + offsety], 36, color),
                           Text2("+Health", [600 + offsetx, 2*400/3 + statOffset + offsety], 36, color),
                           Text2("Revive", [600/3 + offsetx, 400 + statOffset + offsety], 36, color),
                           Text2("Inventory", [2*600/3 + offsetx, 400 + statOffset + offsety], 36, color),
                           Text2("Store", [600 + offsetx, 400 + statOffset + offsety], 36, color)]
            dynamicTexts = [Text2(controls["forward"].upper(), [600/4 + offsetx, 400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["backward"].upper(), [2*600/4 + offsetx, 400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["left"].upper(), [3*600/4 + offsetx, 400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["right"].upper(), [600 + offsetx, 400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["speed"].upper(), [600/4 + offsetx, 2*400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["half"].upper(), [2*600/4 + offsetx, 2*400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["full"].upper(), [3*600/4 + offsetx, 2*400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["health"].upper(), [600 + offsetx, 2*400/3 + dynOffset + offsety], 36, color2),
                            Text2(controls["revive"].upper(), [600/3 + offsetx, 400 + dynOffset + offsety], 36, color2),
                            Text2(controls["inventory"].upper(), [2*600/3 + offsetx, 400 + dynOffset + offsety], 36, color2),
                            Text2(controls["store"].upper(), [600 + offsetx, 400 + dynOffset + offsety], 36, color2)]
            key = ""
            tempKey = False
            index = 0
            viewChanged = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
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
                        controls["revive"] = "v"
                        controls["store"] = "b"
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
            
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
                elif staticTexts[index].baseText.lower() == "speed":
                    controls["speed"] = opt
                elif staticTexts[index].baseText.lower() == "full heal":
                    controls["full"] = opt
                elif staticTexts[index].baseText.lower() == "half heal":
                    controls["half"] = opt
                elif staticTexts[index].baseText.lower() == "+health":
                    controls["health"] = opt
                elif staticTexts[index].baseText.lower() == "revive":
                    controls["revive"] = opt
                elif staticTexts[index].baseText.lower() == "inventory":
                    controls["inventory"] = opt
                elif staticTexts[index].baseText.lower() == "store":
                    controls["store"] = opt
                
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
                if not test:
                    saveMap(user, items, enemies, player, controls)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                            
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()

    if views.top() == "petsSt":
        if viewChanged:
            offsetx = 35
            options = [StoreChoice([900/3 + offsetx, 275], views.top(), "calicoCat"),
                       StoreChoice([2*900/3 - offsetx, 275], views.top(), "owl"),
                       StoreChoice([900/4, 450], views.top(), "blackCat"),
                       StoreChoice([2*900/4, 450], views.top(), "frog"),
                       StoreChoice([3*900/4, 450], views.top(), "raccoon")]
            viewChanged = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
        
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
            choices = []
            index = 0
            factor = 20
            original = [10, 10]
            sub = SettingsButton([200, 700/2 - 50], "back+")
            add = SettingsButton([700, 700/2 - 50], "forward+")
            buy = SettingsButton([900/2, 500], "buy")
            options = SpriteSheetScale("Images/Spritesheets/Store/Spells.png", [original[0]*factor, original[1]*factor], original).load_stripH([0, 0, original[0]*factor, original[1]*factor], 9,  (221, 255, 0))
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                temp += 1
        
        for i in player.inventory["spells"]:
            for c in choices:
                if c == i:
                    choices.remove(c)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if sub.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if buy.click(event.pos):
                        if player.purchase(choices[index] + 1, "spell"):
                            choices.remove(choices[index])
                            if index > 0:
                                index -= 1
                            elif index < 0:
                                index += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(options[choices[index]], [900/2 - (10/2*factor), 200])
        screen.blit(add.image, add.rect)
        screen.blit(sub.image, sub.rect)
        screen.blit(buy.image, buy.rect)
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
                if not test:
                    saveMap(user, items, enemies, player, controls)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                 
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
            offset1 = 188
            offset2 = 74
            options = [StoreChoice([900/2, offset1], "clothesSt", "eyeSt"),
                       StoreChoice([900/2, offset1 + offset2], "clothesSt", "mouthSt"),
                       StoreChoice([900/2, offset1 + offset2*2], "clothesSt", "colorSt"),
                       StoreChoice([900/2, offset1 + offset2*3], "clothesSt", "hatSt"),
                       StoreChoice([900/2, offset1 + offset2*4], "clothesSt", "shirtSt"),
                       StoreChoice([900/2, offset1 + offset2*5], "clothesSt", "glassSt")]
            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
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
                            options = []
                            views.push(option.kind)
                            viewChanged = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
          
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
        
    if views.top() == "eyeSt":
        if viewChanged:
            choices = []
            index = 0
            original = [22, 12]
            factor = 15
            sub = SettingsButton([200, 700/2 - 50], "back+")
            add = SettingsButton([700, 700/2 - 50], "forward+")
            buy = SettingsButton([900/2, 500], "buy")
            options = SpriteSheetScale("Images/Spritesheets/Store/Eye Images.png", [original[0]*factor, original[1]*factor], original).load_stripH([0, 0, original[0]*factor, original[1]*factor], 8,  (221, 255, 0))
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                temp += 1
        
        for i in player.inventory["eyes"]:
            for c in choices:
                if c == i:
                    choices.remove(c)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if sub.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if buy.click(event.pos):
                        if player.purchase(choices[index], "eyes"):
                            if index > 0:
                                index -= 1
                            elif index < 0:
                                index += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(options[choices[index]], [900/2 - (22/2*factor), 200])
        screen.blit(add.image, add.rect)
        screen.blit(sub.image, sub.rect)
        screen.blit(buy.image, buy.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
    
    if views.top() == "mouthSt":
        if viewChanged:
            choices = []
            index = 0
            original = [14, 7]
            factor = 20
            sub = SettingsButton([200, 700/2 - 50], "back+")
            add = SettingsButton([700, 700/2 - 50], "forward+")
            buy = SettingsButton([900/2, 500], "buy")
            options = SpriteSheetScale("Images/Spritesheets/Store/Mouth Images.png", [original[0]*factor, original[1]*factor], original).load_stripH([0, 0, original[0]*factor, original[1]*factor], 8,  (221, 255, 0))
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                temp += 1
        
        for i in player.inventory["mouths"]:
            for c in choices:
                if c == i:
                    choices.remove(c)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if sub.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if buy.click(event.pos):
                        if player.purchase(choices[index], "mouths"):
                            if index > 0:
                                index -= 1
                            elif index < 0:
                                index += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(options[choices[index]], [900/2 - (14/2*factor), 225])
        screen.blit(add.image, add.rect)
        screen.blit(sub.image, sub.rect)
        screen.blit(buy.image, buy.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
    
    if views.top() == "colorSt":
        if viewChanged:
            choices = []
            index = 0
            factor1 = 6
            factor2 = 4
            original = [50, 50]
            sub = SettingsButton([200, 700/2 - 50], "back+")
            add = SettingsButton([700, 700/2 - 50], "forward+")
            buy = SettingsButton([900/2, 500], "buy")
            options = SpriteSheetScale("Images/Spritesheets/Store/Color Images.png", [original[0]*factor1, original[1]*factor2], original).load_stripH([0, 0, original[0]*factor1, original[1]*factor2], 4, (0,0,0))
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                temp += 1
        
        for i in player.inventory["colors"]:
            for c in choices:
                if c == i:
                    choices.remove(c)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if sub.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if buy.click(event.pos):
                        if player.purchase(choices[index], "colors"):
                            if index > 0:
                                index -= 1
                            elif index < 0:
                                index += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(options[choices[index]], [900/2 - (50/2*factor1), 200])
        screen.blit(add.image, add.rect)
        screen.blit(sub.image, sub.rect)
        screen.blit(buy.image, buy.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
    
    if views.top() == "hatSt":
        if viewChanged:
            choices = []
            index = 0
            factor = 10
            original = [28, 17]
            sub = SettingsButton([200, 700/2 - 50], "back+")
            add = SettingsButton([700, 700/2 - 50], "forward+")
            buy = SettingsButton([900/2, 500], "buy")
            options = SpriteSheetScale("Images/Spritesheets/Store/Hat Images.png", [original[0]*factor, original[1]*factor], original).load_stripH([0, 0, original[0]*factor, original[1]*factor], 4,  (221, 255, 0))
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                temp += 1
        
        for i in player.inventory["hats"]:
            for c in choices:
                if (c + 1) == i:
                    choices.remove(c)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if sub.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if buy.click(event.pos):
                        if player.purchase(choices[index] + 1, "hats"):
                            if index > 0:
                                index -= 1
                            elif index < 0:
                                index += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(options[choices[index]], [900/2 - (28/2*factor), 200])
        screen.blit(add.image, add.rect)
        screen.blit(sub.image, sub.rect)
        screen.blit(buy.image, buy.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
    
    if views.top() == "shirtSt":
        if viewChanged:
            choices = []
            index = 0
            factor = 10
            original = [32, 21]
            sub = SettingsButton([200, 700/2 - 50], "back+")
            add = SettingsButton([700, 700/2 - 50], "forward+")
            buy = SettingsButton([900/2, 500], "buy")
            options = SpriteSheetScale("Images/Spritesheets/Store/Shirt Images.png", [original[0]*factor, original[1]*factor], original).load_stripH([0, 0, original[0]*factor, original[1]*factor], 2,  (221, 255, 0))
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                temp += 1
        
        for i in player.inventory["shirts"]:
            for c in choices:
                if (c + 1) == i:
                    choices.remove(c)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if sub.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if buy.click(event.pos):
                        if player.purchase(choices[index] + 1, "shirts"):
                            if index > 0:
                                index -= 1
                            elif index < 0:
                                index += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(options[choices[index]], [900/2 - (32/2*factor), 200])
        screen.blit(add.image, add.rect)
        screen.blit(sub.image, sub.rect)
        screen.blit(buy.image, buy.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
    
    if views.top() == "glassSt":
        if viewChanged:
            choices = []
            index = 0
            factor = 10
            original = [18, 17]
            sub = SettingsButton([200, 700/2 - 50], "back+")
            add = SettingsButton([700, 700/2 - 50], "forward+")
            buy = SettingsButton([900/2, 500], "buy")
            options = SpriteSheetScale("Images/Spritesheets/Store/Glasses Images.png", [original[0]*factor, original[1]*factor], original).load_stripH([0, 0, original[0]*factor, original[1]*factor], 4,  (221, 255, 0))
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                temp += 1
        
        for i in player.inventory["glasses"]:
            for c in choices:
                if (c + 1) == i:
                    choices.remove(c)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if sub.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if buy.click(event.pos):
                        if player.purchase(choices[index] + 1, "glasses"):
                            if index > 0:
                                index -= 1
                            elif index < 0:
                                index += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        money.update(player.inventory["coins"])
  
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(options[choices[index]], [900/2 - (28/2*factor), 200])
        screen.blit(add.image, add.rect)
        screen.blit(sub.image, sub.rect)
        screen.blit(buy.image, buy.rect)
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
                if not test:
                    saveMap(user, items, enemies, player, controls)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)

        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        pygame.display.flip()

    if views.top() == "petsIn":
        if viewChanged:
            offsetx = 35
            options = [InventoryChoice([900/3 + offsetx, 2*700/3], views.top(), "frog"),
                       InventoryChoice([900/4, 700/3 + 25], views.top(), "calicoCat"),
                       InventoryChoice([2*900/3 - offsetx, 2*700/3], views.top(), "raccoon"),
                       InventoryChoice([2*900/4, 700/3 + 25], views.top(), "owl"),
                       InventoryChoice([3*900/4, 700/3 + 25], views.top(), "blackCat")]
            locked = [SettingsButton([900/3 + offsetx, 2*700/3], "locked"),
                      SettingsButton([900/4, 700/3 + 25], "locked"),
                      SettingsButton([2*900/3 - offsetx, 2*700/3], "locked"),
                      SettingsButton([2*900/4, 700/3 + 25], "locked"),
                      SettingsButton([3*900/4, 700/3 + 25], "locked")]
            equipped = [SettingsButton([900/3 + offsetx, 2*700/3], "equipped"),
                        SettingsButton([900/4, 700/3 + 25], "equipped"),
                        SettingsButton([2*900/3 - offsetx, 2*700/3], "equipped"),
                        SettingsButton([2*900/4, 700/3 + 25], "equipped"),
                        SettingsButton([3*900/4, 700/3 + 25], "equipped")]

            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
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
                            if option.kind in player.inventory["pets"]:
                                if petEquip != option.kind:
                                    petEquip = option.kind
                                    pet = Pet([player.rect.center[0] - 1, player.rect.center[1] - 1], petEquip)
                                else:
                                    petEquip = ""
                                    pet = ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
        
        
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for i, option in enumerate(options):
            screen.blit(option.image, option.rect)
            if option.kind not in player.inventory["pets"]:
                screen.blit(locked[i].image, locked[i].rect)
            elif option.kind == petEquip:
                screen.blit(equipped[i].image, equipped[i].rect)
        pygame.display.flip()

    if views.top() == "spellsIn":
        if viewChanged:
            choices = []
            status = []
            equip = None
            index = 0
            original = [10, 10]
            factor = 20
            rect = [900/2 - 10/2*factor, 700/2 + 25 - 10/2*factor]
            options = SpriteSheetScale("Images/Spritesheets/Store/Spells.png", [original[0]*factor, original[1]*factor], original).load_stripH([0, 0, original[0]*factor, original[1]*factor], 9,  (221, 255, 0))
            button = StoreChoice([900/2, 700/2 + 25], "spellsSt", "hidden", factor)
            minus = SettingsButton([900/2 - 200, 700/2 + 25], "back+")
            add = SettingsButton([900/2 + 200, 700/2 + 25], "forward+")
            locked = SettingsButton([900/2, 700/2 + 25], "locked+")
            equipped = SettingsButton([900/2, 700/2 + 25], "equipped+")
            viewChanged = False
            temp = 0
            while temp < len(options):
                choices += [temp]
                status += [0]
                temp += 1
        
        for c in choices:
            there = False
            for i in player.inventory["spells"]:
                if c == i:
                    there = True
            if equip == c:
                status[c] = 2
            elif there:
                status[c] = 0
            else:
                status[c] = 1
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    if add.click(event.pos):
                        if index < len(choices) - 1:
                            index += 1
                        elif index >= len(choices) - 1:
                            index = 0
                    if minus.click(event.pos):
                        if index > 0:
                            index -= 1
                        elif index <= 0:
                            index = len(choices) - 1
                    if button.click(event.pos):
                        if status[index] == 0:
                            equip = index
                        elif status[index] == 2:
                            equip = None
                        else:
                            pass
                            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                                
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        screen.blit(button.image, button.rect)
        screen.blit(options[choices[index]], rect)
        if status[index] == 1:
            screen.blit(locked.image, locked.rect)
        elif status[index] == 2:
            screen.blit(equipped.image, equipped.rect)
        screen.blit(add.image, add.rect)
        screen.blit(minus.image, minus.rect)
        screen.blit(money.image, money.rect)
        pygame.display.flip()
            
    if views.top() == "potionsIn":
        if viewChanged:
            offsetx = 30
            offsety = -50
            options = [InventoryChoice([900/3, 275], views.top(), "fullHeal"),
                       InventoryChoice([2*900/3, 275], views.top(), "halfHeal"),
                       InventoryChoice([900/4, 450], views.top(), "health"),
                       InventoryChoice([900/2, 450], views.top(), "revive"),
                       InventoryChoice([3*900/4, 450], views.top(), "speed")]
            amounts = [Text2("", [900/3 + offsetx + 25, 275 + offsety], 36, "Black"),
                       Text2("", [2*900/3 + offsetx + 25, 275 + offsety], 36, "Black"),
                       Text2("", [900/4 + offsetx + 25, 450 + offsety], 36, "Black"),
                       Text2("", [900/2 + offsetx + 25, 450 + offsety], 36, "Black"),
                       Text2("", [3*900/4 + offsetx + 25, 450 + offsety], 36, "Black")]
            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                        
        for i, option in enumerate(options):
            amounts[i].update(player.inventory[option.kind + "Potion"])
                                
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for option in options:
            screen.blit(option.image, option.rect)
        for amount in amounts:
            screen.blit(amount.image, amount.rect)
        pygame.display.flip()
            
    if views.top() == "clothesIn":
        if viewChanged:
            player.speedx = 0
            player.speedy = 0
            amount = 6
            minX = 400
            yOffset = 150
            yOffset2 = 5
            addX = 700
            textX = 550
            yFactor = 400
            text = {"eye": InventoryChoice([textX, yOffset + yFactor/amount - yOffset2], "clothesIn", "eyes"),
                     "mouth": InventoryChoice([textX, yOffset + 2*yFactor/amount - yOffset2], "clothesIn", "mouth"),
                     "color": InventoryChoice([textX, yOffset + 3*yFactor/amount - yOffset2], "clothesIn", "color"),
                     "hat": InventoryChoice([textX, yOffset + 4*yFactor/amount - yOffset2], "clothesIn", "hat"),
                     "shirt": InventoryChoice([textX, yOffset + 5*yFactor/amount - yOffset2], "clothesIn", "shirt"),
                     "glasses": InventoryChoice([textX, yOffset + 6*yFactor/amount - yOffset2], "clothesIn", "glasses")}
            minus = {"eye": SettingsButton([minX, yOffset + yFactor/amount - yOffset2], "back"),
                     "mouth": SettingsButton([minX, yOffset + 2*yFactor/amount - yOffset2], "back"),
                     "color": SettingsButton([minX, yOffset + 3*yFactor/amount - yOffset2], "back"),
                     "hat": SettingsButton([minX, yOffset + 4*yFactor/amount - yOffset2], "back"),
                     "shirt": SettingsButton([minX, yOffset + 5*yFactor/amount - yOffset2], "back"),
                     "glasses": SettingsButton([minX, yOffset + 6*yFactor/amount - yOffset2], "back")}
            add = {"eye": SettingsButton([addX, yOffset + yFactor/amount - yOffset2], "forward"),
                   "mouth": SettingsButton([addX, yOffset + 2*yFactor/amount - yOffset2], "forward"),
                   "color": SettingsButton([addX, yOffset + 3*yFactor/amount - yOffset2], "forward"),
                   "hat": SettingsButton([addX, yOffset + 4*yFactor/amount - yOffset2], "forward"),
                   "shirt": SettingsButton([addX, yOffset + 5*yFactor/amount - yOffset2], "forward"),
                   "glasses": SettingsButton([addX, yOffset + 6*yFactor/amount - yOffset2], "forward")}
            choices = {"eye": [player.eyeChoice, player.inventory["eyes"]],
                       "mouth": [player.mouthChoice, player.inventory["mouths"]],
                       "color": [player.colorChoice, player.inventory["colors"]],
                       "hat": [player.hatChoice, player.inventory["hats"]],
                       "shirt": [player.shirtChoice, player.inventory["shirts"]],
                       "glasses": [player.glassesChoice, player.inventory["glasses"]]}
            
            viewChanged = False
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not test:
                    saveMap(user, items, enemies, player, controls)
                sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if closeButton.click(event.pos):
                        selected = ""
                        views = Stack("game")
                    if backButton.click(event.pos):
                        views.pop()
                        viewChanged = True
                    for m in minus.keys():
                        if minus[m].click(event.pos):
                            if choices[m][0] > 0:
                                choices[m][0] -= 1
                            else:
                                choices[m][0] = len(choices[m][1]) - 1
                    for a in add.keys():
                        if add[a].click(event.pos):
                            if choices[a][0] < len(choices[a][1]) - 1:
                                choices[a][0] += 1
                            else:
                                choices[a][0] = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup = Popup("escape", [size[0]/2, size[1]/2])
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                if not test:
                                    saveMap(user, items, enemies, player, controls)
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    escape = False
                                    if not test:
                                        saveMap(user, items, enemies, player, controls)
                                    sys.exit()
                                elif event.key == pygame.K_n:
                                    escape = False
                        screen.blit(popup.image, popup.rect)
                        pygame.display.flip()
                        clock.tick(60)
                                        
        player.eyeChoice = choices["eye"][0]
        player.mouthChoice = choices["mouth"][0]
        player.colorChoice = choices["color"][0]
        player.hatChoice = choices["hat"][0]
        player.shirtChoice = choices["shirt"][0]
        player.glassesChoice = choices["glasses"][0]
                        
        player.update(size)
        
        screen.blit(popup[0].image, popup[0].rect)
        screen.blit(pygame.transform.scale(player.image, [player.spriteSize[0] * 3, player.spriteSize[1] * 3]), player.image.get_rect(midtop = [200, 200]))
        screen.blit(closeButton.image, closeButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for t in text.keys():
            screen.blit(text[t].image, text[t].rect)
        for m in minus.keys():
            screen.blit(minus[m].image, minus[m].rect)
        for a in add.keys():
            screen.blit(add[a].image, add[a].rect)
        pygame.display.flip()
