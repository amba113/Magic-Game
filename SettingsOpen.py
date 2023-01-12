import pygame, sys, math, random

class SettingsOpen():

    def __init__(self, pos = [25,25]):
        self.image = pygame.transform.scale(pygame.image.load("Images/Settings.png"), [30, 30])
        
        
        self.rect = self.image.get_rect(center = pos)
        
    def click(self, mousePos):
        if self.rect.left < mousePos[0]:
            if self.rect.right > mousePos[0]:
                if self.rect.bottom > mousePos[1]:
                    if self.rect.top < mousePos[1]:
                        return True
        return False

