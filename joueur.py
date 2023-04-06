# Classe du personnage joueur (la grenouille)

import pygame # Importation de pygame
pygame.mixer.init() # Initialiser le module son de pygame

#from time import sleep  # Importation la fonction sleep du module time afin de ralentir les déplacements du joueur


class Joueur(pygame.sprite.Sprite):
    "Personnage joueur"
    def __init__(self, image, width, height, jump_sound ):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        print(self.image)
        self.jump_sound = pygame.mixer.Sound(jump_sound)  # Son joué lors des déplacements du joueur
    
        self.vies = 3
        self.x = 320# Position x du joueur
        self.y = 420 # Position y du joueur


    def jouer_son_saut(self):
        "Jouer le son de saut du joueur"
        self.jump_sound.play() 
        clock = pygame.time.Clock()
        while pygame.mixer.get_busy():
            clock.tick(10)

    def mettre_a_jour_position(self, key):
        "Mettre à jour la position du joueur"


        if key[pygame.K_UP]: 
            self.y -= 40
            

           # print("y :", self.y)
                
            #print(self.y)
            self.jouer_son_saut()
        

           # sleep(0.01)


        if key[pygame.K_DOWN]:
            self.y += 40
           # print("y :", self.y)
           # print(self.y)

            self.jouer_son_saut()

           # sleep(0.01)

        if key[pygame.K_LEFT]:
            self.x -= 40
            print("x :", self.x)
            print(self.x)
            self.jouer_son_saut()

            #sleep(0.01)

        if key[pygame.K_RIGHT]:
            self.x += 40

           # print("x :", self.x)
           # print(self.x)
            self.jouer_son_saut()

            #sleep(0.01)


        self.rect.x = self.x
        self.rect.y = self.y        




    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))        



        