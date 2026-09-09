# Gérer le temps, les phases...

import pygame

class Time:
    def __init__(self):
        self.heure_depart = pygame.time.get_ticks() # Recupérer l'heure
        self.heure = pygame.time.get_ticks() - self.heure_depart # Avec ce calcul on obtient le temps pendant lequel le jeu à été lancer
        self.time_phase = 10000 # Le temps d'une phase ??
        self.opacite = 0 # 0 pour le jour et 150 pour la nuit
        # Pour gérer l'opacite en fonction de l'heure 0 a midi mais plus sombre la nuit...

        self.phase = 1
        self.jour = self.phase % 2 == 1  # Jour = True si phase impair sinon nuit
        self.jour_etat = "Jour" #Chaine de caractère jour ou nuit


    def changer_phase(self):
        self.phase +=1
        self.jour = self.phase % 2 == 1 
        if self.jour:
            self.opacite = 0
            self.jour_etat = "Jour"
        else:
            self.jour_etat = "Nuit"
            self.opacite = 150

    def update(self):
        self.heure = pygame.time.get_ticks() - self.heure_depart
        #print(self.heure)
