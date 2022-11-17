import pygame, sys, math
from Obstacles import *
from Player import *

def loadMap(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = size/2
    tiles = []
    walls = []
    playerLoc = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
    lines = newLines
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls += [Obstacle([x*size + offset, y*size + offset], "wall")]
            if c == "@":
                walls += [Obstacle([x*size + offset, y*size + offset], "tree")]
            if c == "$":
                playerLoc = [x*size + offset, y*size + offset]
                
    tiles = [walls, 
             playerLoc]
    return tiles

loadMap("Maps/Spawn.lvl")
