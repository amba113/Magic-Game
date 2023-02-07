import pygame, sys, math, random, os

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
length = 500
rect1 = pygame.rect.Rect(100,100, 500, 50)
rect2 = pygame.rect.Rect(100,100, length, 50)
inc = False
screen = pygame.display.set_mode(size)
go = True
while True:
    if go == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    go = False
                    
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (0, 255, 0), rect2, 0, 5)
        pygame.draw.rect(screen, (255,255,255), rect1, 3, 5)

        if length <= 1:
            inc = True
        elif length > 500:
            inc = False
            length = 500
        
        if length > 1 and length <= 500 and inc == False:
            length -= 1
        elif length >= 1 and length <= 500 and inc == True:
            length += 1
        
        print(length)        
            
        rect2 = pygame.rect.Rect(100,100, length, 50)
        
    elif go == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    go = True
    pygame.display.flip()
    clock.tick(60)
    
