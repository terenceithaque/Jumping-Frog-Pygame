# Programme principal du jeu

import pygame # Importation du module pygame
from decor import *
from joueur import *
from voiture import *
from random import randrange
import time



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
joueur.getScore()  # Obtenir le score enregistré dans le fichier score.txt

image_voiture = "assets/images/voiture.png" # Chemin vers l'image de la voiture



is_running = True # Le jeu est-il en cours d'exécution ?


voitures = pygame.sprite.Group()  # Créer un groupe pour stocker les voitures
voitures.add(Voiture(image_voiture, 75, 75))

temps_dernier_passage_voiture = time.time()  # Temps écoulé depuis le dernier passage d'une voiture

game_over = False




while is_running: # Tant que le jeu est exécuté
   
   
    
    for evenement in pygame.event.get():
        if evenement == pygame.QUIT:
            is_running = False

    touche_pressee = pygame.key.get_pressed()   # Verifier la touche pressée

    joueur.mettre_a_jour_position(touche_pressee)
    joueur.draw(screen)
    #joueur.afficher_pourcent_vie(screen) # Afficher le pourcentage de vies du joueur
    
     
    # Dessiner les objets du jeu
    screen.fill((255,255,255))
    decor.draw(screen)
    screen.blit(joueur.image, joueur.rect, joueur.afficher_pourcent_vie(screen))

    current_time = time.time()

    for voiture in voitures:
        pygame.time.wait(100)
        Voiture.add(Voiture(image_voiture, 75, 75))

        if voiture.rect.right < 0:
            voitures.remove(voiture)
            pygame.time.wait(100)
            voitures.add(Voiture(image_voiture, 75, 75))        

        if joueur.rect.colliderect(voiture.rect):
            print("Le joueur est entré en collision avec une voiture")
            joueur.perdre_vie(1, screen) # Réduire la vie du joueur à chaque fois qu'il entre en collision avec une voiture
            print(joueur.vies, "vies restantes")
            joueur.score -= 10 # Réduire le score actuel du joueur
            print(joueur.score)
        
           

            joueur.x = 320  # Repositionner le joueur à sa position initiale
            joueur.y = 420
        voiture.avancer()
        voiture.draw(screen)
        # voiture.supprimer()

        


        if joueur.vies <= 0:  # Si le nombre de points de vie restants est inférieur ou égal à zéro

           joueur.kill()
           joueur.game_over(screen) # Afficher le message de game over
   
           
           is_running  = False
           


   
        if is_running:

            # Mettre à jour l'écran
            pygame.display.flip()    


pygame.mixer.quit()            


