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

color = (255, 255, 255)
box1 = False
box2 = False
box3 = False
new = False

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
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if box1:
                    userText1 = userText1[:-1]
                elif box2:
                    userText2 = userText2[:-1]
                elif box3:
                    userText3 = userText3[:-1]
            elif event.key == pygame.K_RETURN:
                direct1 = "logins.txt"
                f1 = open(direct1, 'r')
                lines1 = f1.readlines()
                direct2 = "usernames.txt"
                f2 = open(direct2, 'r')
                lines2 = f2.readlines()
                user = ""
                username = ""
                newLines1 = []
                good = False
                for l in lines1:
                    newLine1 = l.split("    ")
                    newLines1 += [newLine1]
                newLines2 = []
                for l in lines2:
                    newLine2 = l.split("    ")
                    newLines2 += [newLine2]
                                    
                for i, line1 in enumerate(newLines1):
                    for x, line2 in enumerate(newLines2):
                        if userText1 == line1[0]:
                            if userText2 + "\n" == line1[1]:
                                good = True
                            else:
                                userText1 = ""
                                userText2 = ""
                                userText3 = ""
                                good = False
                                print("no match")
                            new = False
                        else:
                            new = True
                            
                        if good == True:
                            temp = newLines1[i]
                            user = temp[0]
                            username = temp[1]
                f1.close()
                f2.close()
                print("User: " + user, "\nName: " + username)
                            
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
        if new:
            a1 = open(direct1, 'a')
            a2 = open(direct2, 'a')
            add1 = userText1 + "    " + userText2
            add2 = userText1 + "    " + userText3
            print(add1, "\n", add2)
            a1.write(add1)
            a2.write(add2)
            print(a1, "\n", a2)
            a1.close()
            a2.close()
            label3 = baseFont.render("Screen Name:", True, (0,0,0))
            textSurface3 = baseFont.render(userText3, True, color)
            pygame.draw.rect(screen, (0, 0, 0), inputRect3)
            screen.blit(textSurface3, (inputRect3.x+5, inputRec3.y+5))
            screen.blit(label3, (inputRect3.x, inputRect3.y - 30))
                
    screen.fill(color)
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
