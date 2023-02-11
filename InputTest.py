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
    direct = "logins.txt"
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
                print(user, username)
                if name:
                    add = userText1 + " " + userText2 + " " + userText3 + "\n"
                    
                    direct = "logins.txt"
                    a = open(direct, 'a')
                    a.write(add)
                    a.close()
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
