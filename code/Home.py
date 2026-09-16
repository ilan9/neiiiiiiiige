import pygame

class Home():
    def __init__(self):
        self.life = 100
        self.life_max = 100 # en fonction du level de la maison ??
        self.level = 0

    def hurt(self,damage): #Pour que la maison perde des PV
        self.life -= damage
        if self.life <= 0 :
            print("Défaite la maison n'as plus de vie !!")

    def healing(self,heal): # Pour que la maison gagne des PV
        if self.life > 0:
            self.life += heal
            self.life = min(self.life,self.life_max) # max de vie a max_life