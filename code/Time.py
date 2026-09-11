# Gérer le temps, les phases...

import pygame

class Time:
    def __init__(self):
        self.time_start = pygame.time.get_ticks() # Recupérer l'time
        self.time = pygame.time.get_ticks() - self.time_start # Avec ce calcul on obtient le temps pendant lequel le jeu à été lancer
        self.time_phase = 10000 # Le temps d'une phase ??
        self.opacity = 0 # 0 pour le day et 150 pour la nuit
        # Pour gérer l'opacity en fonction de l'time 0 a midi mais plus sombre la nuit...

        self.phase = 1
        self.day = self.phase % 2 == 1  # day = True si phase impair sinon nuit
        self.day_etat = "Jour" #Chaine de caractère day ou nuit


    def change_phase(self):
        self.phase +=1
        self.day = self.phase % 2 == 1 
        if self.day:
            self.opacity = 0
            self.day_etat = "Jour"
        else:
            self.day_etat = "Nuit"
            self.opacity = 150

    def update(self):
        self.time = pygame.time.get_ticks() - self.time_start
        #print(self.time)
