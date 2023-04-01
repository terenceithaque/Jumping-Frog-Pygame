# Classe du personnage joueur (la grenouille)

import pygame # Importation de pygame


class Joueur(pygame.sprite.Sprite):
    "Personnage joueur"
    def __init__(self, image, width, height):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        print(self.image)
        self.vies = 3
        self.x = 0# Position x du joueur
        self.y = 0 # Position y du joueur

    def mettre_a_jour_position(self, key):
        "Mettre à jour la position du joueur"


        if key[pygame.K_UP]:    
            self.y -= 5
            print("y :", self.y)
                
            print(self.y)

        if key[pygame.K_DOWN]:
            self.y += 5
            print("y :", self.y)
            print(self.y)

        if key[pygame.K_LEFT]:
            self.x -= 5
            print("x :", self.x)
            print(self.x)

        if key[pygame.K_RIGHT]:
            self.x += 5
            print("x :", self.x)
            print(self.x)


        self.rect.x = self.x
        self.rect.y = self.y        




    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))        



        