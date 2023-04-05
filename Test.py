import pygame, sys, math, random, os, pickle, pillow

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

image = pillow.open("Images/Eye Spritesheet.png")
rect = self.image.get_rect(center = startPos)

image.ImageColor.hsl(200, 100%, 50%)

screen.blit(image, rect)

pygame.display.flip()
clock.tick(60)
