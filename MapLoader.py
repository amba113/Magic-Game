import pygame, sys, math
from Obstacles import *
from Player import *

def loadMap(coord = [1, 1], enter = "def"):
    direct = "Rooms/" + str(coord[1]) + str(coord[0]) + ".lvl"
    f = open(direct, 'r')
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
            if c == "-":
                walls += [Obstacle([x*size + 2*offset, y*size], "TB")]
            if c == "_":
                walls += [Obstacle([x*size + 2*offset, y*size + 2*offset], "TB")]
            if c == "|":
                walls += [Obstacle([x*size, y*size + 2*offset], "LR")]
            if c == "/":
                walls += [Obstacle([x*size - 2*offset, y*size + 2*offset], "LR")]
            if enter == "def" and c == "$":
                playerLoc = [x*size + offset, y*size + offset]
            elif enter == "top" and c == "%":
                playerLoc = [x*size + 2*offset, y*size + 2*offset]
            elif enter == "bottom" and c == "&":
                playerLoc = [x*size + 2*offset, y*size + -offset]
            elif enter == "left" and c == "(":
                playerLoc = [x*size + 2*offset, y*size + 2*offset]
            elif enter == "right" and c == ")":
                playerLoc = [x*size + -offset, y*size + 2*offset]
                
    tiles = [walls, 
             playerLoc]
    return tiles
