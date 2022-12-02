import pygame, sys, math, random
from Player import *
from MapLoader import *
from Obstacles import *

pygame.init()

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

counter = 0

tiles = loadMap()
walls = tiles[0]
doors = tiles[1]
player = Player(2, tiles[2])
players = [player]
items = tiles[3]

loc = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player.sprint(True)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player.sprint(False)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                player.useItem("f")
                print("Health:", player.hp)
            elif event.key == pygame.K_h:
                player.useItem("h")
                print("Health:", player.hp)
            elif event.key == pygame.K_g:
                player.useItem("g")
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player.goto(tiles[2])
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                item.wandChoice(1)
            elif event.key == pygame.K_2:
                item.wandChoice(2)
                
    for wall in walls:
        player.wallTileCollide(wall)
    
    for item in items:
        if player.itemCollide(item):
            items.remove(item)
    
    player.update(size)
    
    for door in doors:
        if player.doorCollide(door):
            loc = door.kind
            tiles = loadMap(player.coord, loc)
            
            walls = tiles[0]
            doors = tiles[1]
            items = tiles[3]
            
            player.goto(tiles[2]) #relocate player

    screen.fill((250, 175, 225))
    for wall in walls:
            screen.blit(wall.image, wall.rect)
    for item in items:
            screen.blit(item.image, item.rect)
    for door in doors:
            screen.blit(door.image, door.rect)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(60)
