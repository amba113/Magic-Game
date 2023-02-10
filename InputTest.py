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
inputRect1 = pygame.Rect(size[0]/2, size[1]/3, 150, 50)
inputRect2 = pygame.Rect(size[0]/2, 2*size[1]/3, 150, 50)

color = (255, 255, 255)
box1 = False
box2 = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect1.collidepoint(event.pos):
                box1 = True
                box2 = False
            elif inputRect2.collidepoint(event.pos):
                box1 = False
                box2 = True
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if box1:
                    userText1 = userText1[:-1]
                elif box2:
                    userText2 = userText2[:-1]
            elif event.key == pygame.K_RETURN:
                print(userText1, userText2)
            elif event.key == pygame.K_TAB:
                if box1:
                    box1 = False
                    box2 = True
                elif box2:
                    box2 = False
                    box1 = True
            else:
                if box1:
                    userText1 += event.unicode
                elif box2:
                    userText2 += event.unicode
                
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
