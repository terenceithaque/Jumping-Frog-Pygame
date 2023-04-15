# Voitures du jeu, qui servent d'obstacles que le joueur doit éviter
import pygame # Importer le module pygame
from random import randrange  # Importer la fonction randrange du module random

class Voiture(pygame.sprite.Sprite):
    "Voiture"
    def __init__(self, image,width, height):
        super().__init__() # Appeler le constructeur de la classe parente
        self.image = pygame.image.load(image) # Charger l'image de la voiture
       # print(self.image)
        self.image = pygame.transform.scale(self.image, (width, height)) # Redimensionner l'image de la voiture en fonction de la largeur et de la hauteur données en paramètres
        self.rect = self.image.get_rect()
        self.vitesse = randrange(25, 70) # Tirer au sort la vitesse de la voiture
       # print(self.vitesse)
        self.rect.x = 920 # Position x de la voiture
        #print(self.rect.x)
        self.rect.y = 220 # Position y de la voiture
        #print(self.rect.y)
        #print(self.temps_dernier_passage)


    def supprimer(self):
        if self.rect.x <= 0:
            self.kill()
           # print("Voiture supprimée !")

    
    def avancer(self):
        self.rect.x -= self.vitesse
        #print(self.x, self.y)

    

        



   

    def draw(self, screen):
        screen.blit(self.image, self.rect)


                        

        