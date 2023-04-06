# Programme principal du jeu

import pygame # Importation du module pygame
from decor import *
from joueur import *
from voiture import *
from time import sleep
from random import randrange


pygame.init() # Initialisation du module pygame
pygame.mixer.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jumping Frog en Python")

image_decor = "assets/images/road.png"  # Image représentant le décor du jeu
decor_x = 800
decor_y = 500
vitesse_decor = 5

decor = Decor(image_decor, decor_x, decor_y)

chemin_musique_jeu = "assets/sons_et_musiques/Michael Jackson - Thriller - Thriller [ZEHsIcsjtdI].webm.mp3" # Chemin vers la musique du jeu

pygame.mixer.music.load(chemin_musique_jeu)
pygame.mixer.music.play(-1)  # Jouer la musique principale du jeu


image_joueur = "assets/joueur/joueur.png"
son_saut_joueur = "assets/sons_et_musiques/saut_joueur.mp3"
joueur = Joueur(image_joueur, 50, 50, son_saut_joueur)

image_voiture = "assets/images/voiture.png" # Chemin vers l'image de la voiture



is_running = True # Le jeu est-il en cours d'exécution ?


voitures = pygame.sprite.Group()  # Créer un groupe pour stocker les voitures
voitures.add(Voiture(image_voiture, 75, 75))


while is_running: # Tant que le jeu est exécuté


   
    
    for evenement in pygame.event.get():
        if evenement == pygame.QUIT:
            is_running = False

    touche_pressee = pygame.key.get_pressed()   # Verifier la touche pressée

    joueur.mettre_a_jour_position(touche_pressee)

    
     
    # Dessiner les objets du jeu
    screen.fill((255,255,255))
    decor.draw(screen)
    screen.blit(joueur.image, joueur.rect)

    for voiture in voitures:
        if joueur.rect.colliderect(voiture.rect):
            print("Le joueur est entré en collision avec une voiture")
            joueur.vies -= 1
            print(joueur.vies)
        
           

            joueur.x = 320  # Repositionner le joueur à sa position initiale
            joueur.y = 420
        voiture.avancer()
        voiture.draw(screen)
        # voiture.supprimer()

        if voiture.rect.right < 0:
            voitures.remove(voiture)
            voitures.add(Voiture(image_voiture, 75, 75))


        if joueur.vies <= 0:
            pygame.quit()
            print("Vous êtes mort(e) !")     



   


    # Mettre à jour l'écran
    pygame.display.flip()    


pygame.mixer.music.stop()        
