# Programme principal du jeu

import pygame # Importation du module pygame
from decor import *

pygame.init() # Initialisation du module pygame

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jumping Frog en Python")

image_decor = "assets/images/road.png"  # Image représentant le décor du jeu
decor_x = 800
decor_y = 500
vitesse_decor = 5

decor = Decor(image_decor, decor_x, decor_y)

is_running = True # Le jeu est-il en cours d'exécution ?

while is_running: # Tant que le jeu est exécuté
   
    
    for evenement in pygame.event.get():
        if evenement == pygame.QUIT:
            is_running = False


    # Dessiner les objets du jeu
    screen.fill((255,255,255))
    decor.draw(screen)

    # Mettre à jour l'écran
    pygame.display.flip()        
