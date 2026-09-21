import pygame

class Home():
    def __init__(self,rect:pygame.rect):
        self.life = 100
        self.life_max = 100 # en fonction du level de la maison ??
        self.level = 0
        self.rect : pygame.rect = rect

    def hurt(self,damage): #Pour que la maison perde des PV
        self.life -= damage
        if self.life <= 0 :
            print("Défaite la maison n'as plus de vie !!")
        else:
            print("La maison a pris des dégats il lui reste "+str(self.life)+" PV.")

    def healing(self,heal): # Pour que la maison gagne des PV
        if self.life > 0:
            self.life += heal
            self.life = min(self.life,self.life_max) # max de vie a max_life