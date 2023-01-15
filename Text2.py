import pygame, sys, math

class Text2():
    def __init__(self, baseText, startPos = [0,0], size = 48, color = [0,0,0]):
        self.color = color
        self.font = pygame.font.Font(None, size)
        self.baseText = baseText
        self.image = self.font.render("HP: 100", 1, color)
        self.rect = self.image.get_rect(center = startPos)
        
    def update(self, hp):
        text = self.baseText + str(hp)
        self.image = self.font.render(text, 1, self.color)
        self.rect = self.image.get_rect(center = self.rect.center)
