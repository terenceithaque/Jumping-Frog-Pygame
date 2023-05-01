# Classe du personnage joueur (la grenouille)
from tkinter import messagebox
import pygame # Importation de pygame
import os # Importer les fonctions du système d'exploitation de l'ordinateur du joueur
pygame.mixer.init() # Initialiser le module son de pygame

#from time import sleep  # Importation la fonction sleep du module time afin de ralentir les déplacements du joueur


class Joueur(pygame.sprite.Sprite):
    "Personnage joueur"
    def __init__(self, image, width, height, jump_sound ):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        print(self.image)
        self.jump_sound = pygame.mixer.Sound(jump_sound)  # Son joué lors des déplacements du joueur
        self.vies = 3  # Nombre de points de vie  du joueur
        self.max_vies = 3 # Nombre de vies maximales du joueur
        self.font = pygame.font.Font(None, 36)
        self.game_over_font = pygame.font.Font(None, 36)
        self.score_font = pygame.font.Font(None, 36)
        self.best_score_font = pygame.font.Font(None, 36)
    
        self.x = 320# Position x du joueur
        print(self.x)
        self.y = 420 # Position y du joueur
        print(self.y)

        self.score = 0 # Score du joueurs

        self.best_score = self.score # Score maximum du joueur

        self.score_filename = "score.txt"  # Ouvrir le fichier score.txt afin d'y des modifications

   
    
   


    def perdre_vie(self, degats, screen):
        "Faire prendre des dégats au joueur"
        self.vies -= degats
        self.afficher_pourcent_vie(screen)


    def afficher_pourcent_vie(self, screen):
       
        pourcentage_vie_restante = round(self.vies / self.max_vies * 100)  # Pourcentage de vies qu'il reste à l'écran
        str_pourcentage_vie_restante = "{} % vies".format(str(pourcentage_vie_restante))# Convertir le pourcentage de vies restantes en une chaine de caractères
        
        self.display_surface = self.font.render(str_pourcentage_vie_restante, True, (255, 255, 255))
        #print(self.display_surface)
        #sprint(str_pourcentage_vie_restante)

        screen.blit(self.display_surface, (0, 0))
   


    def jouer_son_saut(self):
        "Jouer le son de saut du joueur"
        self.jump_sound.play(maxtime= 100) 
        clock = pygame.time.Clock()
        while pygame.mixer.get_busy():
            clock.tick(10)

    def mettre_a_jour_position(self, key):
        "Mettre à jour la position du joueur"


        if key[pygame.K_UP]: 
            pygame.time.wait(2)
            self.y -= 40
            

            print("y :", self.y)
                
           # print(self.y)
            self.jouer_son_saut()
        

           # sleep(0.01)


        if key[pygame.K_DOWN]:
            pygame.time.wait(2)
            self.y += 40
            print("y :", self.y)
           # print(self.y)

            self.jouer_son_saut()

           # sleep(0.01)

        if key[pygame.K_LEFT]:
            pygame.time.wait(2)
            self.x -= 40
            print("x :", self.x)
            #print(self.x)
            self.jouer_son_saut()

            #sleep(0.01)

        if key[pygame.K_RIGHT]:
            pygame.time.wait(2)
            self.x += 40

            print("x :", self.x)
            #print(self.x)
            self.jouer_son_saut()

            #sleep(0.01)


        self.rect.x = self.x
        self.rect.y = self.y        


    def saveScore(self):
       "Sauvegarder le score du joueur dans un fichier texte"
       if self.score > self.best_score: # Si le score actuel est supérieur au meilleur score
            try:
                if os.path.getsize(self.score_filename) > 0:
                    open(self.score_filename, "w").truncate(0)

                with open(self.score_filename, "w") as wf:    
                    wf.write(str(self.score))  # Ecrire le score de la partie dans le fichier score.txt
                    wf.close()

                return self.score        

            except IOError:
                 messagebox.showerror("Erreur d'écriture du score", "Le nouveau score n'a pas pu être écrit correctement.")

           # finally: # En cas d'erreur critique
             #     messagebox.showwarning("Fermeture en raison d'erreur critique", "Le jeu va être fermé en raison de la détection d'une erreur critique. Le score actuel sera perdu lors de la fermeture du jeu.")
              #    pygame.quit() # Fermer Pygame       


       else:  # Dans les autres cas
            try:
               if  os.path.getsize(self.score_filename) > 0:
                    open(self.score_filename, "w").truncate(0)

               with open(self.score_filename, "w") as wf:  
                    wf.write(str(self.best_score)) # Ecrire le meilleur score dans score.txt
                    wf.close()

               return self.best_score     


            except IOError:
               messagebox.showerror("Erreur d'écriture du meilleur score", "Le meilleur score n'a pas pu être écrit correctement.")        
                    
           

           

           # finally:
             #    messagebox.showwarning("Fermeture en raison d'erreur critique", "Le jeu va être fermé en raison de la détection d'une erreur critique. Le score actuel sera perdu lors de la fermeture du jeu.")
              #   pygame.quit() # Fermer Pygame


    def getScore(self):
        "Récuperer le score sauvegardé"
        rf = open(self.score_filename, "r") # Lire le fichier score.txt. rf = read file
        if os.path.getsize(self.score_filename) > 0: # Si la taille du fichier score.txt est supérieure à 0 octets
            score_trouve = int(rf.readline()) # Convertir le score trouvé dans le fichier score.txt en un nombre entier
            #print("Score trouvé :", score_trouve)
            return score_trouve



    def checkScore(self):
        "Vérifier le score du joueur"
        if self.score > self.best_score:
            self.best_score = self.score
            print("Meilleur score :", self.best_score)
        
        return self.best_score




    def displayScore(self, screen):
        "Afficher le score du joueur"
        score = "Score : {}".format(str(self.score))
        self.afficher_score = self.score_font.render(score, True, (200, 200, 200))
        #print(self.afficher_score)
        screen.blit(self.afficher_score, (0, 20))
        if self.checkScore() >= self.getScore():  
            meilleur_score = "Meilleur score : {}".format(str(self.checkScore()))
            print("Meilleur score :", meilleur_score)
            self.afficher_meilleur_score = self.best_score_font.render(meilleur_score, True, (150, 150, 150))
            screen.blit(self.afficher_meilleur_score, (0, 60))


            








    
    def game_over(self, screen):
       "Terminer la partie dès que le joueur a perdu"
        
       game_over_text = "Vous êtes mort(e) ! Score réalisé {}".format(self.score)

       self.display_game_over_text = self.game_over_font.render(game_over_text, True, (255, 255, 255))

       screen.blit(self.display_game_over_text, (400, 400))

       self.saveScore()


    def reinitialiserPositions(self):
        "Réinitialiser les positions x et y de départ du joueur"
        self.x = 320
        self.y = 420 



                            
            
    

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
                



        
