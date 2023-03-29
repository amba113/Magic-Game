import pygame, sys, math, random, os, pickle

class SpriteSheet:

    def __init__(self, direct, basic):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(direct + "/" + basic).convert()
            self.hats = pygame.image.load(direct + "/" + "Hat " + basic).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {direct}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image1 = pygame.Surface(rect.size).convert()
        image1.blit(self.sheet, (0, 0), rect)
        image2 = pygame.Surface(pygame.Rect([36, 0, 36, 90]).size).convert()
        image2.blit(self.hats, (0, 0), pygame.Rect([36, 0, 36, 90]))
        if colorkey != None:
            if colorkey != -1:
                colorkey = image1.get_at((0,0))
            image1.set_colorkey(colorkey, pygame.RLEACCEL)
            image2.set_colorkey(colorkey, pygame.RLEACCEL)
        image1.blit(image2, (0, 0))
        return image1
    
    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]


    def load_stripH(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
        
    def load_stripV(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0], rect[1]+rect[3]*y, rect[2], rect[3])
                for y in range(image_count)]
        return self.images_at(tups, colorkey)
