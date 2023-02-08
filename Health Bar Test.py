import pygame, sys, math, random, os
from ColorLibrary import *

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()
color = (0, 255, 0)
size = [900, 700]
cRad = 5
height = 25
lengthMax = 500
length = lengthMax
if cRad < height:
    lengthMin = cRad * 2
else:
    lengthMin = cRad
step = 10
rect1 = pygame.rect.Rect(100, 100, lengthMax, height)
rect2 = pygame.rect.Rect(100, 100, length, height)
inc = False
screen = pygame.display.set_mode(size)
go = True
hurt = False
while True:
    if go == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    go = False
                if event.key == pygame.K_a:
                    hurt = True
                    
        screen.fill((0,0,0))
        pygame.draw.rect(screen, color, rect2, 0, cRad)
        pygame.draw.rect(screen, (255,255,255), rect1, 3, cRad)

        if length <= lengthMin:
            inc = True
        elif length > lengthMax:
            inc = False
            length = lengthMax
        
        if length > lengthMin and length <= lengthMax and inc == False and hurt == True:
            length -= step
        elif length >= lengthMin and length <= lengthMax and inc == True and hurt == True:
            length = lengthMin
            print("Death")
                    
        rect2 = pygame.rect.Rect(100, 100, length, height)
        
        color = smoothColor((255, 0, 0), (255, 100, 0), (255, 255, 0), (0, 255, 0), length, lengthMax - lengthMin)
        
        hurt = False
        
    elif go == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    go = True
    pygame.display.flip()
    clock.tick(60)
    
