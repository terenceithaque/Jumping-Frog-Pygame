# Balles que le joueur doit attraper pour augmenter son score
import pygame
from random import randrange

class Balle(pygame.sprite.Sprite):
    "Balles du jeu"

    def __init__(self, image, width, height):
        super().__init__() 
        self.image = pygame.image.load(image)  # Charger l'image de la balle
        self.image_visible = True # Est-ce que l'image de la Balle est visible à l'écran ?
        print(self.image)
        self.image = pygame.transform.scale(self.image, (width, height))  # Adapter la taille de l'image selon les paramètres width et height
        self.rect = self.image.get_rect()
        self.rect.x = randrange(200, 400, step=40)
        print(self.rect.x)
        self.rect.y = randrange(0, 80, step=40)
        print(self.rect.y)


        


    def supprimer(self):
       "Retirer l'image de la balle du jeu"
       #self.remove_internal(group)
       #self.image_visible = False 
       print("Sprite supprimé !")
       self.kill()
       #self.rect.()    


    def draw(self, screen):
        "Dessiner la balle sur l'écran"
       # if self.image_visible: # Si l'image peut être visible
        screen.blit(self.image, self.rect)

