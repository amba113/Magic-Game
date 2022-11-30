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
    doors = []
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
            if enter == "def" and c == "$":
                playerLoc = [x*size + offset, y*size + offset]
            elif enter == "bottom" and c == "%":
                playerLoc = [x*size + 2*offset, y*size + offset]
            elif enter == "top" and c == "&":
                playerLoc = [x*size + 2*offset, y*size + offset]
            elif (enter == "right" or enter == "portal1") and c == "(":
                playerLoc = [x*size + offset, y*size + 2*offset]
            elif (enter == "left" or enter == "portal2") and c == ")":
                playerLoc = [x*size + offset, y*size + 2*offset]

    tiles = [walls,
             doors,
             playerLoc]
    return tiles
