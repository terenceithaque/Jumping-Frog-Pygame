# Décor du jeu
import pygame

import pygame

class Decor:
    "Décor du jeu"
    def __init__(self, image, width, height):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = 0
        self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


  

    def draw(self, ecran):
        ecran.blit(self.image, (self.x, self.y))      