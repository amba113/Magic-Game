import pygame, sys, math
from Obstacles import *
from Player import *
from Items import *

def saveMap(items, coord = [1, 1]):
    outList = []
    for row in range(14):
        outRow = []
        for col in range(18):
            outRow += [" "]
        outList += [outRow]
    
    size = 50
    offset = size/2
    for item in items:
        x = int((item.rect.centerx - offset)/size)
        y = int((item.rect.centery - offset)/size)
        print(x,y, item.kind, item.char)
        outList[y][x] = item.char
        
    out = ""
    for row in range(len(outList)):
        for col in range(len(outList[row])):
            out += outList[row][col]
        out += '\n'
    
    direct = "Rooms/" + str(coord[1]) + str(coord[0]) + ".sav"
    f = open(direct, 'w')
    f.write(out)
    f.close()

def loadMap(coord = [1, 1], enter = "def"):
    direct = "Rooms/" + str(coord[1]) + str(coord[0]) + ".lvl"
    f = open(direct, 'r')
    lines = f.readlines()
    f.close()
    
    direct2 = "Rooms/" + str(coord[1]) + str(coord[0]) + ".itm"
    g = open(direct2, 'r')
    lines2 = g.readlines()
    g.close()
    
    size = 50
    offset = size/2
    tiles = []
    walls = []
    doors = []
    playerLoc = []
    items = []
    
    newLines = []
    newLines2 = []
    
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
            if c == "*":
                walls += [Obstacle([x*size + offset, y*size + offset], "cactus")]
            if c == "-":
                doors += [Obstacle([x*size + 2*offset, y*size + offset], "top")]
            if c == "_":
                doors += [Obstacle([x*size + 2*offset, y*size + offset], "bottom")]
            if c == "|":
                doors += [Obstacle([x*size + offset, y*size + 2*offset], "left")]
            if c == "/":
                doors += [Obstacle([x*size + offset, y*size + 2*offset], "right")]
            if c == "0":
                doors += [Obstacle([x*size + offset, y*size + 2*offset], "portal1")]
            if c == "O":
                doors += [Obstacle([x*size + offset, y*size + 2*offset], "portal2")]
            if c == "X":
                doors += [Obstacle([x*size + 2*offset, y*size + offset], "tutent")]
            if c == "x":
                doors += [Obstacle([x*size + 2*offset, y*size + offset], "tutext")]
            if c == "$" and enter == "def":
                playerLoc = [x*size + offset, y*size + offset]
            elif c == "%" and (enter == "bottom" or enter == "tutext"):
                playerLoc = [x*size + 2*offset, y*size + offset]
            elif c == "&" and(enter == "top" or enter == "tutent"):
                playerLoc = [x*size + 2*offset, y*size + offset]
            elif c == "(" and (enter == "right" or enter == "portal1"):
                playerLoc = [x*size + offset, y*size + 2*offset]
            elif c == ")" and (enter == "left" or enter == "portal2"):
                playerLoc = [x*size + offset, y*size + 2*offset]
            
    for line in lines2:
        newLine2 = ""
        for c in line:
            if c != "\n":
                newLine2 += c
        newLines2 += [newLine2]
    lines2 = newLines2       
    
    for y, line in enumerate(lines2):
        for x, c in enumerate(line):
            if c == "!":
                items += [Item([x*size + offset, y*size + offset], "wand", '!')]
            if c == ";":
                items += [Item([x*size + offset, y*size + offset], "halfPotion", ';')]
            if c == ":":
                items += [Item([x*size + offset, y*size + offset], "fullPotion", ':')]
            if c == "~":
                items += [Item([x*size + offset, y*size + offset], "speedPotion", '~')]
            if c == "^":
                items += [Item([x*size + offset, y*size + offset], "revivePotion", '^')]
            if c == "?":
                items += [Item([x*size + offset, y*size + offset], "healthPotion", '?')]
            
    tiles = [walls,
             doors,
             playerLoc,
             items]

    return tiles
    
