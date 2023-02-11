import pygame, sys, math, random, os

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

baseFont = pygame.font.Font(None, 40)
userText1 = ''
userText2 = ''
userText3 = ''
inputRect1 = pygame.Rect(size[0]/2, size[1]/4, 150, 50)
inputRect2 = pygame.Rect(size[0]/2, 2*size[1]/4, 150, 50)
inputRect3 = pygame.Rect(size[0]/2, 3*size[1]/4, 150, 50)
agreeRect = pygame.Rect(size[0]/2, size[1]/3, 150, 50)
disagreeRect = pygame.Rect(size[0]/2, 2*size[1]/3, 150, 50)


color = (255, 255, 255)
box1 = False
box2 = False
box3 = False
name = False
add = False
agree = False

def doSignin(name, pwd):
    print(name, pwd)
    direct1 = "logins.txt"
    f1 = open(direct1, 'r')
    lines1 = f1.readlines()
    f1.close()
    
    direct2 = "usernames.txt"
    f2 = open(direct2, 'r')
    lines2 = f2.readlines()
    f2.close()
    
    user = None
    username = None
    newLines1 = []
    newLines2 = []
    good = False
    new = False
    
    for l in lines1:
        newLine1 = l.split(" ")
        newLines1 += [newLine1]
        
    for l in lines2:
        newLine2 = l.split(" ")
        newLines2 += [newLine2]
    z = 0
    for i, line1 in enumerate(newLines1):
        for x, line2 in enumerate(newLines2):
            if name == line1[0]:
                if pwd == line1[1]:
                    z = i
                    good = True
                else:
                    good = False
                    print("no match")
                new = False
            else:
                new = True
                
            if good == True:
                temp = newLines2[z]
                user = temp[0]
                username = temp[1]

    f1.close()
    f2.close()
    return user, username, new
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect1.collidepoint(event.pos):
                box1 = True
                box2 = False
                box3 = False
            elif inputRect2.collidepoint(event.pos):
                box1 = False
                box2 = True
                box3 = False
            elif inputRect3.collidepoint(event.pos):
                box1 = False
                box2 = False
                box3 = True
            elif agreeRect.collidepoint(event.pos):
                agree = True
            elif disagreeRect.collidepoint(event.pos):
                agree = False
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if box1:
                    userText1 = userText1[:-1]
                elif box2:
                    userText2 = userText2[:-1]
                elif box3:
                    userText3 = userText3[:-1]
            elif event.key == pygame.K_RETURN:
                user, username, new = doSignin(userText1, userText2)
                if name:
                    add1 = userText1 + " " + userText2 + "\n"
                    add2 = userText1 + " " + userText3 + "\n"
                    
                    direct1 = "logins.txt"
                    direct2 = "usernames.txt"
                    a1 = open(direct1, 'a')
                    a2 = open(direct2, 'a')
                    a1.write(add1)
                    a2.write(add2)
                    a1.close()
                    a2.close()
                    name = False
                    
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
                                                
            elif event.key == pygame.K_TAB:
                if box1:
                    box1 = False
                    box2 = True
                    box3 = False
                elif box2:
                    box1 = False
                    box2 = False
                    box3 = True
                elif box3:
                    box1 = True
                    box2 = False
                    box3 = False
            else:
                if box1:
                    userText1 += event.unicode
                elif box2:
                    userText2 += event.unicode
                elif box3:
                    userText3 += event.unicode
                    
    screen.fill(color)
    if add and agree:
        label3 = baseFont.render("Screen Name:", True, (0,0,0))
        textSurface3 = baseFont.render(userText3, True, color)
        pygame.draw.rect(screen, (0, 0, 0), inputRect3)
        screen.blit(textSurface3, (inputRect3.x+5, inputRect3.y+5))
        screen.blit(label3, (inputRect3.x, inputRect3.y - 30))
        name = True
    elif add and not agree:
        yes = baseFont.render("Yes", True, color)
        no = baseFont.render("No", True, color)
        warn = baseFont.render("This account does not exist, make a new one?", True, (0,0,0))
        pygame.draw.rect(screen, (0, 0, 0), agreeRect)
        pygame.draw.rect(screen, (0, 0, 0), disagreeRect)
        screen.blit(yes, (agreeRect.x+5, agreeRect.y+5))
        screen.blit(no, (disagreeRect.x+5, disagreeRect.y+5))
        screen.blit(warn, (100, 100))
    elif not add and not agree:
        label1 = baseFont.render("Username:", True, (0,0,0))
        textSurface1 = baseFont.render(userText1, True, color)
        pygame.draw.rect(screen, (0, 0, 0), inputRect1)
        screen.blit(textSurface1, (inputRect1.x+5, inputRect1.y+5))
        screen.blit(label1, (inputRect1.x, inputRect1.y - 30))
        
        label2 = baseFont.render("Password:", True, (0,0,0))
        textSurface2 = baseFont.render(userText2, True, color)
        pygame.draw.rect(screen, (0, 0, 0), inputRect2)
        screen.blit(textSurface2, (inputRect2.x+5, inputRect2.y+5))
        screen.blit(label2, (inputRect2.x, inputRect2.y - 30))
    
    pygame.display.flip()
    clock.tick(60)
